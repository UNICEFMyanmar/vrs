from __future__ import unicode_literals

from itertools import chain

from django import forms
from django.forms import ModelForm, CharField, Textarea, ValidationError
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django_select2.widgets import Select2Widget

from .models import F101, F201, RHC, Hospital
from .permissions import check_location


def fields_with_choices(model):
    fields = []
    for field in sorted(model._meta.get_fields()):
        if hasattr(field, 'choices'):
            if len(field.choices):
                fields.append(field.name)
    return fields


class _Select2Widget(Select2Widget):


    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
            return format_html('<option value="{}"{}>{}</option>',
                           option_value,
                           selected_html,
                           force_text(option_label))
        else:
            return ""


    def render_options(self, choices, selected_choices):

        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
        return ''.join(output)


class F101Form(ModelForm):
    class Meta:
        model = F101
        exclude = ['deleted', 'NRYY', 'NRMM', 'NDYY', 'NDMM']

        widgets = dict(
            (field, Select2Widget())
            for field in fields_with_choices(F101)
        )
        widgets.update(
            {
                'Informer': Textarea,
                'RCIR': Textarea,
                'RHC': _Select2Widget,
                'Hospital': Select2Widget
            }
        )

    def __init__(self, user=None, *args, **kwargs):
        super(F101Form, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['NAGP_M'].widget.attrs['readonly'] = True

        self.fields['Date_of_Registration'].widget.format = '%d%m%Y'
        self.fields['Date_of_Registration'].input_formats = ['%d%m%Y', '%d%m%y']

        self.fields['Date_of_Birth'].widget.format = '%d%m%Y'
        self.fields['Date_of_Birth'].input_formats = ['%d%m%Y', '%d%m%y']

        self.fields['Hospital'].choices = Hospital.objects.birth_as_choices()

    def clean(self):
        super(F101Form, self).clean()

        if self.user and not check_location(
                self.user,
                (self.cleaned_data.get('ST_DV', 0),
                 self.cleaned_data.get('DIS', 0),
                 self.cleaned_data.get('TWN', 0))
        ):
            raise ValidationError(_('You are not allowed to create or edit entries for this region'))

        return self.cleaned_data


class F101UpdateForm(F101Form):
    comment = CharField(
        widget=Textarea,
        label=_("Reason for edit:"),
        required=True
    )


class F101DeleteForm(F101UpdateForm):
    def __init__(self, *args, **kwargs):
        super(F101DeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "comment":
                self.fields[field].widget.attrs['readonly'] = True
                self.fields[field].required = False


class F201Form(ModelForm):
    class Meta:
        model = F201
        exclude = ['deleted', 'DDY', 'DDM', 'DRY', 'DRM']

        widgets = dict(
            (field, Select2Widget())
            for field in fields_with_choices(F201)
        )
        widgets.update(
            {
                'RCIR': Textarea,
                'Informant_name': Textarea,
                'RHC': _Select2Widget,
                'Hospital': Select2Widget,
                'AGE_CODE': forms.HiddenInput(),
                'EXTRA_AGE_CODE': forms.HiddenInput()
            }
        )

    def __init__(self, user=None, *args, **kwargs):
        super(F201Form, self).__init__(*args, **kwargs)
        self.user = user

        self.fields['Date_of_Registration'].widget.format = '%d%m%Y'
        self.fields['Date_of_Registration'].input_formats = ['%d%m%Y', '%d%m%y']

        self.fields['Date_of_Death'].widget.format = '%d%m%Y'
        self.fields['Date_of_Death'].input_formats = ['%d%m%Y', '%d%m%y']

        self.fields['Hospital'].choices = Hospital.objects.death_as_choices()

    def clean(self):

        super(F201Form, self).clean()

        if self.user and not check_location(
                self.user,
                (self.cleaned_data.get('NNRT', 0),
                 self.cleaned_data.get('NNRT1', 0),
                 self.cleaned_data.get('NNST', 0))
        ):
            raise ValidationError(_('You are not allowed to create or edit entries for this region'))

        return self.cleaned_data


class F201UpdateForm(F201Form):
    comment = CharField(
        widget=Textarea,
        label=_("Reason for edit:"),
        required=True
    )


class F201DeleteForm(F201UpdateForm):
    def __init__(self, *args, **kwargs):
        super(F201DeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "comment":
                self.fields[field].widget.attrs['readonly'] = True
                self.fields[field].required = False