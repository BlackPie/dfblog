from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30)
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    password1 = forms.CharField(label=_("Password"), max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(label=_("Password again"), max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(label=_("Email"), required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = reverse_lazy('signup')
    helper.layout = Layout(
        'username',
        'first_name',
        'last_name',
        'password1',
        'password2',
        'email',
        FormActions(Submit('signup', 'Create an account', css_class='btn-primary form-button'))
    )

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("passwords dont match each other")
        return self.cleaned_data


class SigninForm(AuthenticationForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = reverse_lazy('signin')
    helper.layout = Layout(
        'username',
        'password',
        FormActions(Submit('signin', 'Sign In', css_class='btn-primary form-button'))
    )
