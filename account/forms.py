from django import forms
from . models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        self.fields['special_user'].disabled=True


    class Meta:
        model=User
        fields=['username','email','first_name','last_name','special_user','profile_pic']




class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')