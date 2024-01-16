from django import forms

from apps.models import UserModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('name', 'position', 'image', 'facebook', 'twitter','linkedin')
        # exclude = ('created_at',)