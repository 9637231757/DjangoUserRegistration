from django import forms
from  .models import forms           

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','photo','email','password','mobile_number','date_of_birth']
        widgets = {
            'date_of_birth' : forms.DateInput(attr={'type': 'date'}),
            'password': forms.PasswordInput(),
        }