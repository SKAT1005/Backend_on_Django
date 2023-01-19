from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Почта'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Введите пароль повторно'


class EmailForm(forms.Form):
    email = forms.CharField(max_length=1024)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=1024)

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'


class UserEditForm(forms.ModelForm):
    file = forms.ImageField(widget=forms.ClearableFileInput, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    username = forms.EmailField(max_length=1024, required=False)
    first_name = forms.CharField(max_length=256, required=False)

    class Meta:
        model = User
        fields = ('email',)


class OrderForm(forms.ModelForm):
    DELIVERY_CHOICES = (('1', 'Обычная доставка'),
                        ('2', 'Экспресс доставка'))
    PAY_CHOICES = (('1', 'Онлайн картой'),
                   ('2', 'Онлайн со случайного чужого счета'))
    phone_number = forms.CharField(max_length=32, required=False)
    city = forms.CharField(max_length=256, required=False)
    address = forms.CharField(max_length=1024, required=False)
    first_name = forms.CharField(max_length=1024, required=False)

    class Meta:
        model = User
        fields = ('email',)