from django.contrib import admin
from django.contrib.admin.utils import unquote, quote
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.formats import localize
from reversion.models import Version
import reversion
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from .models import F101, F201, Profile, RHC, Hospital
from .permissions import get_user_location_names

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'ST_DV', 'DIS', 'TWN', 'birth', 'death')
    ordering = ('ST_DV', 'DIS', 'TWN', 'code')
    search_fields = ['name']
    list_filter = ('ST_DV', 'DIS', 'TWN')

admin.site.register(Hospital, HospitalAdmin)


class RHCAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'ST_DV', 'DIS', 'TWN')
    ordering = ('ST_DV', 'DIS', 'TWN', 'RHC')
    search_fields = ['Village']
    list_filter = ('ST_DV', 'DIS', 'TWN')

admin.site.register(RHC, RHCAdmin)


class FormAdmin(reversion.VersionAdmin):
    date_hierarchy = 'updated_at'
    preserve_filters = True

    def history_url_field(self, obj):
        # noinspection PyProtectedMember
        opts = self.model._meta
        return "<a href=%s>%s</a>" % (
            reverse(
                "%s:%s_%s_history" % (self.admin_site.name, opts.app_label, opts.model_name),
                args=(quote(obj.pk),)), render_to_string('history_link.html'))

    history_url_field.allow_tags = True
    history_url_field.short_description = ''

    class Media:
        js = ('js/admin/fixes.js',)
        css = {
            'all': ('css/admin/fixes.css',)
        }

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj:
            with reversion.create_revision():
                obj.save(DO_NOT_UPDATE_UPDATE_AT=True)
                reversion.set_comment(_("Opened by admin"))
        return super(FormAdmin, self).render_change_form(request, context, add, change, form_url, obj)

    def revision_view(self, request, object_id, version_id, extra_context=None):
        object_id = unquote(object_id)  # Underscores in primary key get quoted to "_5F"
        obj = get_object_or_404(self.model, pk=object_id)
        version = get_object_or_404(Version, pk=version_id, object_id=force_text(obj.pk))
        created_date = localize(version.revision.date_created)

        with reversion.create_revision():
            obj.save()
            reversion.set_comment(_("Revision (%s) %s opened by admin") % (version.revision.pk, created_date))
        return super(FormAdmin, self).revision_view(request, object_id, version_id, extra_context)


class F101Admin(FormAdmin):
    list_display = (
        'id', 'ST_DV', 'DIS', 'TWN', 'NOPR', 'updated_at', 'deleted',
        'history_url_field')


class F201Admin(FormAdmin):
    list_display = (
        'id', 'NNRT', 'NNRT1', 'NNST', 'OPR', 'updated_at', 'deleted',
        'history_url_field')


admin.site.register(F101, F101Admin)
admin.site.register(F201, F201Admin)


class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link

    object_link.allow_tags = True
    object_link.short_description = _("History")

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)

from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib import admin


def roles(self):
    short_name = unicode  # function to get group name
    # short_name = lambda x:unicode(x)[:1].upper() # first letter of a group
    p = sorted([u"<a title='%s'>%s</a>" % (x, short_name(x)) for x in self.groups.all()])
    if self.user_permissions.count(): p += ['+']
    value = ', '.join(p)
    return mark_safe("<nobr>%s</nobr>" % value)


roles.allow_tags = True
roles.short_description = u'Groups'


def last(self):
    if self.last_login:
        fmt = "%b %d, %H:%M"
        value = self.last_login.strftime(fmt)
        return mark_safe("<nobr>%s</nobr>" % value)
    else:
        return ""


last.allow_tags = True
last.admin_order_field = 'last_login'


def adm(self):
    return self.is_superuser


adm.boolean = True
adm.admin_order_field = 'is_superuser'


def staff(self):
    return self.is_staff


staff.boolean = True
staff.admin_order_field = 'is_staff'

from django.core.urlresolvers import reverse


def persons(self):
    return ', '.join(['<a href="%s">%s</a>' % (reverse('admin:auth_user_change', args=(x.id,)), x.username) for x in
                      self.user_set.all().order_by('username')])


persons.allow_tags = True


class ProfileAdmin(admin.TabularInline):
    model = Profile


def limited_permissions_forms_only(permissions):
    permissions.queryset = permissions.queryset.filter(
        content_type__model__in=('f101', 'f201', 'f103', 'f203')
    ).order_by('name')


class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', staff, adm, roles, last, 'locations']
    list_filter = ['groups', 'is_staff', 'is_superuser', 'is_active']
    readonly_fields = ('locations',)
    fieldsets = (
        (
            _('User'), {
                'fields': ('username', 'password'),
                'classes': ('grp-collapse grp-closed',),
            }
        ),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_("Authority"), {"classes": ("placeholder profile-group",), "fields": ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Applied permissions'), {'fields': ('locations',)}),
        (
            _('Important dates'),
            {
                'fields': ('last_login', 'date_joined'),
                'classes': ('grp-collapse grp-closed',),
            },

        ),
    )

    inlines = [ProfileAdmin, ]

    def locations(self, obj):
        return '<br/>'.join(get_user_location_names(obj))

    locations.allow_tags = True

    def get_form(self, request, obj=None, **kwargs):
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        if 'user_permissions' in form.base_fields and not request.user.is_superuser:
            limited_permissions_forms_only(form.base_fields['user_permissions'])

        return form

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdmin(GroupAdmin):
    list_display = ['name', persons]
    list_display_links = ['name']

    def get_form(self, request, obj=None, **kwargs):
        form = super(GroupAdmin, self).get_form(request, obj, **kwargs)
        if 'permissions' in form.base_fields and not request.user.is_superuser:
            limited_permissions_forms_only(form.base_fields['permissions'])
        return form

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
