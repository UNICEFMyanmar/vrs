from django.contrib import admin
from birth_registration.admin import FormAdmin
from certification.models import F103, F203


class F103Admin(FormAdmin):
    readonly_fields = F103._meta.get_all_field_names()
    date_hierarchy = 'created_at'
    list_display = (
        'id', 'ST_DV', 'DIS', 'TWN', 'NOPR', 'created_at', 'history_url_field')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return  request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False


class F203Admin(FormAdmin):
    readonly_fields = F203._meta.get_all_field_names()
    date_hierarchy = 'created_at'
    list_display = (
        'id', 'NNRT', 'NNRT1', 'NNST', 'OPR', 'created_at', 'history_url_field')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return  request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(F103, F103Admin)
admin.site.register(F203, F203Admin)
