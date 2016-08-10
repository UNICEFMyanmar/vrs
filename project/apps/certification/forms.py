from django import forms
from django.core.exceptions import ValidationError
from birth_registration.codes import BORN_DEAD
from certification.models import F103, F203
from django.utils.translation import ugettext_lazy as _

class FormCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

    def clean(self):
        if self.errors:
            raise ValidationError(
                _('You need to correct the original F101 form'))

        return self.cleaned_data


class F103CreateForm(FormCreateForm):
    class Meta:
        model = F103
        fields = [field.name for field in model._meta.fields if field.editable]
        widgets = {field: forms.TextInput for field in fields if field not in ('RCIR', 'Informer')}

    def clean(self):
        super(F103CreateForm, self).clean()
        if self.cleaned_data.get('f101').NBTH == BORN_DEAD:
            raise ValidationError(
                _('According to the original F101 form, the child was born dead')
            )

        return self.cleaned_data


class F203CreateForm(FormCreateForm):
    class Meta:
        model = F203
        fields = [field.name for field in model._meta.fields if field.editable]
        widgets = {field: forms.TextInput for field in fields if field not in ('Informant_name',)}


class F103Form(forms.ModelForm):
    class Meta:
        model = F103
        exclude = ()

class F203Form(forms.ModelForm):
    class Meta:
        model = F203
        exclude = ()

