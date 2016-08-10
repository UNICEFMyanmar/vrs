from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import CreateView, DetailView
from django.utils.translation import ugettext_lazy as _, ungettext, ugettext
from django_tables2 import SingleTableView, RequestConfig
from birth_registration.models import F101, F201
from birth_registration.views import CreateReversionOnGetMixin, AppliedPermissionMixin
from certification.filters import F103Filter, F203Filter
from certification.forms import F103CreateForm, F103Form, F203CreateForm, F203Form
from certification.tables import F103Table, F203Table
from .models import F103, F203


class F103CreateView(CreateView):
    form_class = F103CreateForm

    model = F103
    ref_model = F101

    FormListView = "F103ListView"
    F103DetailView = "F103DetailView"
    F103PrintView = "F103PrintView"
    NOPR = 'NOPR'

    def __init__(self, **kwargs):
        super(F103CreateView, self).__init__(**kwargs)
        self.excluded = ('id', self.NOPR)
        self.ref_model_name = self.ref_model._meta.model_name

    def get(self, request, *args, **kwargs):
        
        if self.model.objects.filter(**{self.ref_model_name: self.kwargs[self.ref_model_name]}).exists():
            count = self.model.objects.filter(**{self.ref_model_name: self.kwargs[self.ref_model_name]}).count()
            messages.warning(request, ungettext(
                'There is already a certificate related to this registration',
                'There are  already %(count)d certificates related to this registration',
                count) % {'count': count} + " - <a class='alert-link' href=%s>" % (
                reverse(self.FormListView) + "?" + self.ref_model_name + "=" + self.kwargs[self.ref_model_name],) + ugettext("browse") + "</a>")
            
        return super(F103CreateView, self).get(self, request, *args, **kwargs)

    def pre_populate_same_fields(self, real_ref_model):

        try:
            ref_object = self.ref_model.objects.get_queryset_for_user(self.request.user).get(pk=self.kwargs[self.ref_model_name])
        except ObjectDoesNotExist:
            raise Http404(_('Original form was not found'))

        if real_ref_model:
            fields = {self.ref_model_name: ref_object}
        else:
            fields = {self.ref_model_name: ref_object.id}

        ref_model_fields = [field.name for field in ref_object._meta.fields]

        for field in self.model._meta.fields:
            if field.name in ref_model_fields and field.name not in self.excluded:
                fields[field.name] = getattr(ref_object, field.name)

        return fields

    def get_initial(self):
        return self.pre_populate_same_fields(False)

    def form_valid(self, form):

        # ignore the changes
        fields = self.pre_populate_same_fields(True)
        for field in fields:
            setattr(form.instance, field, fields[field])

        setattr(form.instance, self.NOPR, self.request.user)

        return super(F103CreateView, self).form_valid(form)

    def get_success_url(self):
        if 'print' in self.request.POST:
            return reverse(self.F103PrintView, args=(self.object.id,))
        else:
            return reverse(self.F103DetailView, args=(self.object.id,))


class F203CreateView(F103CreateView):
    form_class = F203CreateForm

    model = F203
    ref_model = F201

    FormListView = "F203ListView"
    F103DetailView = "F203DetailView"
    F103PrintView = "F203PrintView"
    NOPR = 'OPR'


class F103DetailView(DetailView, CreateReversionOnGetMixin, AppliedPermissionMixin):
    model = F103
    form_class = F103Form


class F203DetailView(DetailView, CreateReversionOnGetMixin, AppliedPermissionMixin):
    model = F203
    form_class = F203Form


class F103ListView(SingleTableView):
    model = F103
    table_class = F103Table
    filter = F103Filter

    def get_queryset(self, **kwargs):
        return self.model.objects.get_queryset_for_user(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(F103ListView, self).get_context_data(**kwargs)

        f = self.filter(
            self.request.GET,
            queryset=self.get_queryset(**kwargs)
        )

        table = self.table_class(f.qs)

        RequestConfig(self.request).configure(table)

        context['filter'] = f
        context['table'] = table

        return context


class F203ListView(F103ListView):
    model = F203
    table_class = F203Table
    filter = F203Filter


class F103PrintView(DetailView, CreateReversionOnGetMixin, AppliedPermissionMixin):
    model = F103
    form_class = F103Form
    template_name = "certification/f103_print.html"

class F203PrintView(DetailView, CreateReversionOnGetMixin, AppliedPermissionMixin):
    model = F203
    form_class = F203Form
    template_name = "certification/f203_print.html"
