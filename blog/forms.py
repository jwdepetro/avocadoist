"""
Defines the forms for the blog module.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField, ReCaptchaV3


class CommentForm(forms.Form):
    """
    Defines the form for the comment.

    This form is used by anonymous users on the website to comment on posts.
    """
    name = forms.CharField(
        label=_('Name'), max_length=30, required=True, widget=forms.TextInput(attrs={
            'placeholder': _('Name*'),
            'class': 'form-control'
        }))
    comment = forms.CharField(
        label=_('Comment'), max_length=100, required=True, widget=forms.Textarea(attrs={
            'placeholder': _('Comment*'),
            'size': 100,
            'class': 'form-control',
            'rows': 2
        }))
    captcha = ReCaptchaField(widget=ReCaptchaV3)
