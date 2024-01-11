from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class StyleMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in stop_words:
            if word in cleaned_data:
                raise forms.ValidationError('Вы использовали запрещенное слово в наименовании продукта')
        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in stop_words:
            if word in cleaned_data:
                raise forms.ValidationError('Вы использовали запрещенное слово названии версии')
        return cleaned_data


class ModerationForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)