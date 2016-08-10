import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.utils.text import get_text_list
from django.views.decorators.cache import never_cache, cache_page
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.detail import SingleObjectMixin, BaseDetailView
from django.views.generic.edit import ModelFormMixin
from django_tables2 import SingleTableView, RequestConfig
from django.utils.translation import ugettext_lazy as _, ugettext
import reversion
from .models import F101, F201, RHC
from .filters import F101Filter, F201Filter
from .forms import F101Form, F101UpdateForm, F101DeleteForm, F201Form, F201UpdateForm, F201DeleteForm
from .permissions import get_user_locations, get_user_location_names
from .tables import F101Table, F101RestoreTable, F201Table, F201RestoreTable


def login_form_page(request, template_name='page_home.html'):
    if request.user.is_authenticated():
        return render_to_response(template_name, context_instance=RequestContext(request))
    return login(request, template_name=template_name)


class AppliedPermissionMixin(SingleObjectMixin):
    def get_queryset(self, **kwargs):
        return self.model.objects.get_queryset_for_user(self.request.user, **kwargs)


class FormWithUserMixin(ModelFormMixin):
    def get_form_kwargs(self):
        kwargs = super(FormWithUserMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):

        context = super(FormWithUserMixin, self).get_context_data(**kwargs)
        model_name = self.model._meta.model_name

        context['user_can_delete'] = self.request.user.has_perm("birth_registration.delete_%s" % model_name )
        context['user_can_change'] = self.request.user.has_perm("birth_registration.change_%s" % model_name )

        return context


class F101List(SingleTableView):
    model = F101
    template_name = 'form_list.html'
    table_class = F101Table
    _deleted = False

    def get_queryset(self, **kwargs):
        return F101.objects.get_queryset_for_user(self.request.user).filter(deleted=self._deleted)

    def get_context_data(self, **kwargs):
        context = super(F101List, self).get_context_data(**kwargs)

        f = F101Filter(
            self.request.GET,
            queryset=self.get_queryset(**kwargs)
        )

        table = self.table_class(f.qs)

        RequestConfig(self.request).configure(table)

        context['filter'] = f
        context['table'] = table

        return context


class F101Deleted(F101List):
    table_class = F101RestoreTable
    _deleted = True


class F101Create(CreateView, FormWithUserMixin):
    form_class = F101Form
    model = F101
    template_name = 'form_create.html'

    def get_success_url(self):
        if 'continue' in self.request.POST:
            return reverse_lazy('F101Create')
        elif 'go_to_form'  in self.request.POST:
            return reverse('F101Detail', kwargs={'pk':self.object.id})
        else:
            return reverse_lazy('F101List')

    def form_valid(self, form):
        form.instance.NOPR = self.request.user
        return super(F101Create, self).form_valid(form)


class F101CreateOffline(F101Create):
    template_name = 'form_create_offline.html'

    def post(self, request, *args, **kwargs):
        return render_to_response("500.html",
                                  context_instance=RequestContext(request))


class CreateReversionOnSaveMixin(ModelFormMixin):
    def form_valid(self, form):

        form.changed_data.remove("comment")
        if form.changed_data:
            comment = _('Changed %s, ') % get_text_list(form.changed_data, _('and'))
        else:
            comment = _("No fields changed, ")
        with reversion.create_revision():
            reversion.set_comment(u"%s Reason: %s" % (comment, form.cleaned_data['comment']))

        return super(CreateReversionOnSaveMixin, self).form_valid(form)


class CreateReversionOnGetMixin(BaseDetailView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        with reversion.create_revision():
            if hasattr(self.object, "updated_at"):
                self.object.save(DO_NOT_UPDATE_UPDATE_AT=True)
            else:
                self.object.save()
            reversion.set_comment(_("Opened"))

        form = self.form_class(data=model_to_dict(self.object))
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


class F101Edit(UpdateView, AppliedPermissionMixin, FormWithUserMixin, CreateReversionOnSaveMixin, CreateReversionOnGetMixin):
    model = F101
    form_class = F101UpdateForm
    template_name = 'form_edit.html'

    def form_valid(self, form):
        self.success_url = reverse_lazy('F101Detail', args=[self.object.pk])
        return super(F101Edit, self).form_valid(form)


class F101Detail(DetailView, AppliedPermissionMixin, CreateReversionOnGetMixin, FormWithUserMixin):
    model = F101
    form_class = F101Form
    template_name = 'form_detail.html'
    success_url = reverse_lazy('F101List')


class CreateReversionOnDeleteMixin(ModelFormMixin):
    def form_valid(self, form):
        deleted = self.get_object().deleted
        if deleted:
            comment = ugettext("Restored")
        else:
            comment = ugettext("Deleted")
        form.instance.deleted = not deleted
        with reversion.create_revision():
            reversion.set_comment(u"%s: %s" % (comment, form.cleaned_data['comment']))
        return super(CreateReversionOnDeleteMixin, self).form_valid(form)


class F101Delete(UpdateView, AppliedPermissionMixin, FormWithUserMixin, CreateReversionOnDeleteMixin):
    model = F101
    form_class = F101DeleteForm
    template_name = "form_confirm_delete.html"
    success_url = reverse_lazy("F101List")
    # todo: ignore changes


class F201Create(CreateView, FormWithUserMixin):
    form_class = F201Form
    model = F201
    template_name = 'form_create.html'

    def get_success_url(self):
        if 'continue' in self.request.POST:
            return reverse_lazy('F201Create')
        elif 'go_to_form'  in self.request.POST:
            return reverse('F201Detail', kwargs={'pk':self.object.id})
        else:
            return reverse_lazy('F201List')

    def form_valid(self, form):
        form.instance.OPR = self.request.user
        return super(F201Create, self).form_valid(form)


class F201List(SingleTableView):
    model = F201
    template_name = 'form_list.html'
    table_class = F201Table
    _deleted = False

    def get_queryset(self, **kwargs):
        return F201.objects.get_queryset_for_user(self.request.user).filter(deleted=self._deleted)

    def get_context_data(self, **kwargs):
        context = super(F201List, self).get_context_data(**kwargs)

        f = F201Filter(
            self.request.GET,
            queryset=self.get_queryset(**kwargs)
        )

        table = self.table_class(f.qs)

        RequestConfig(self.request).configure(table)

        context['filter'] = f
        context['table'] = table

        return context


class F201Edit(UpdateView, AppliedPermissionMixin, FormWithUserMixin, CreateReversionOnSaveMixin, CreateReversionOnGetMixin):
    model = F201
    form_class = F201UpdateForm
    template_name = 'form_edit.html'

    def form_valid(self, form):
        self.success_url = reverse_lazy('F201Detail', args=[self.object.pk])
        return super(F201Edit, self).form_valid(form)


class F201Detail(DetailView, AppliedPermissionMixin, CreateReversionOnGetMixin, FormWithUserMixin):
    model = F201
    form_class = F201Form
    template_name = 'form_detail.html'
    success_url = reverse_lazy('F201List')


class F201Delete(UpdateView, AppliedPermissionMixin, FormWithUserMixin, CreateReversionOnDeleteMixin):
    model = F201
    form_class = F201DeleteForm
    template_name = "form_confirm_delete.html"
    success_url = reverse_lazy("F201List")


class F201Deleted(F201List):
    table_class = F201RestoreTable
    _deleted = True


class F201CreateOffline(F201Create):
    template_name = 'form_create_offline.html'

    def post(self, request, *args, **kwargs):
        return render_to_response("500.html",
                                  context_instance=RequestContext(request))


@login_required
def get_locations(request):
    # todo: use it! refs #124
    return HttpResponse(json.dumps(get_user_locations(request.user)), mimetype='application/json')


@login_required
def profile(request):
    permissions = filter(lambda x: any(substring in x for substring in ['_f101', '_f201', '_f103', '_f203']),
                         list(request.user.get_all_permissions()))
    permissions = sorted(permissions, key=lambda s: s[-3:])
    permissions = map(lambda x: x.split(".")[1].split("_"), permissions)
    permissions = [{'verb': ugettext(elem[0].capitalize()), 'model': elem[1].upper()} for elem in permissions]

    locations = [i.split(" - ") for i in get_user_location_names(request.user)]

    return render(request, dictionary={'locations': locations,
                                       'permissions': permissions},
                  template_name='page_profile.html')


def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: :template:`500.html`
    Context: None
    """
    template = loader.get_template(template_name)
    return HttpResponseServerError(template.render(request=request))


@never_cache
def webapp2_appcache(request):
    COOKIE_NAME = 'offline_mode_enabled'
    COOKIE_VALUE = request.COOKIES.get(COOKIE_NAME, "disabled")

    if COOKIE_VALUE == "disable":
        COOKIE_VALUE = "disabled"
    elif COOKIE_VALUE == "enable":
        COOKIE_VALUE = "enabled"

    template = loader.get_template("webapp2." + COOKIE_VALUE)
    response = HttpResponse(template.render(request=request))
    response.set_cookie(COOKIE_NAME, COOKIE_VALUE)
    return response


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise) or isinstance(obj, RHC):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


@cache_page(60*60)
def RHC_choices(request):
    return HttpResponse(
        json.dumps(RHC.objects.as_choices(), cls=LazyEncoder),
                   content_type="application/json")

