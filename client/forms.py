from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label=_("Parol takrorlash"))

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError(_('Parol bir xil emas'))
        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': _('login'),
            'password': _('parol')
        }
        help_texts = {
            'username': _('Login hariflar belgilar ishlatishiz lozim')
        }
        widgets = {
            'password': forms.PasswordInput
        }



