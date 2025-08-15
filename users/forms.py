from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, label='Номер телефона', required=False, help_text='Необязательное поле. Введите ваш номер телефона.')
    username = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'country', 'phone_number', 'avatar' ]
        labels = {'email' : 'E-mail',
                  'username' : 'Имя пользователя',
                  'password1' : 'Пароль',
                  'password2' : 'Подтверждение пароля',
                  'first_name' : 'Имя',
                  'last_name' : 'Фамилия',
                  'country' : 'Страна',
                  'phone_number' : 'Номер телефона',
                  'avatar' : 'Аватар'}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя пользователя'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ваше имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ваша фамилия'})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Страна'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Номер телефона'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Аватар'})

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять из цифр')
        return phone_number


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'country', 'avatar', 'phone_number']
        REQUIRED_FIELDS = ['email', 'username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя пользователя'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ваше имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ваша фамилия'})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Страна'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Номер телефона'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Аватар'})

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять из цифр')
        return phone_number