from django import forms
from django.contrib.auth.models import User
from .models import Cat, Booking

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'date_of_birth', 'gender', 'color', 'vaccination_status']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cat', 'check_in_date', 'check_out_date', 'special_requests']
