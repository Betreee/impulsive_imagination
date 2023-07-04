from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(max_length=254, help_text='Required. A valid email address.')
    password1 = forms.CharField(max_length=128, help_text='Required. 8 characters or more.')
    password2 = forms.CharField(max_length=128, help_text='Required. Enter the same password again.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise forms.ValidationError('This username is already taken.')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise forms.ValidationError('This email is already taken.')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('The two passwords do not match.')

    def save(self, commit=True):
        print(super().clean())
        
        if super().clean() and commit==False:
            user = super().save(commit=False)
            user.set_username(self.cleaned_data['username'])
            user.set_email(self.cleaned_data['email'])

            user.set_password(self.cleaned_data['password1'])
            return user
        if commit and super().clean():
           user =  super().save()
        return user 
    
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 
'bio',
'profile_pic',
'first_name',
'last_name',
'address',
'city',
'state',
'zipcode',
'phone',
'age',
'birth_date',

]
    def update(self,commit=True):
        print(super().clean())
        
        if super().clean() and commit==False:
            user = super().save(commit=False)
            user.set_username(self.cleaned_data['username'])
            user.set_email(self.cleaned_data['email'])
            user.set_address(self.cleaned_data['address'])
            user.set_city(self.cleaned_data['city'])
            user.set_state(self.cleaned_data['state'])
            user.set_zipcode(self.cleaned_data['zipcode'])
            user.set_phone(self.cleaned_data['phone'])
            user.set_bio(self.cleaned_data['bio'])
            user.set_profile_pic(self.cleaned_data['profile_pic'])
            user.set_age(self.cleaned_data['age'])
            user.set_birth_date(self.cleaned_data['birth_date'])
            user.set_password(self.cleaned_data['password1'])
            return user
        if commit and super().clean():
           user =  super().save()
        return user 
        pass