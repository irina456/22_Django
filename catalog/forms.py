from django import forms
from django.core.exceptions import ValidationError
import os
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'boolean_value']
        exclude = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название товара'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Описание Товара'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Категория'})
        self.fields['boolean_value'].widget.attrs.update({'class': 'form-check', 'placeholder': 'Булева переменная'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Изображение товара'})


    BAD_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.BAD_WORDS:
            if word in name.lower():
                raise ValidationError(f'Название продукта содержит запрещенные слова {self.BAD_WORDS}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.BAD_WORDS:
            if word in description.lower():
                raise ValidationError(f'Описание продукта содержит запрещенные слова {self.BAD_WORDS}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        valid_extensions = ['.jpg', '.jpeg', '.png']
        extension = os.path.splitext(image.name)[1].lower()
        if extension not in valid_extensions:
            raise ValidationError(f'Недопустимый формат файла, разрешены форматы: {valid_extensions}')

        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise ValidationError('Файл слишком большой. Максимальный размер 5 Мб')
        return image
