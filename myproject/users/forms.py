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
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user 
    
    def password_check(self, password):
        password1 = self.cleaned_data['password1']

        print(password1)




        #ensure password is 8 characters or more
        if len(password1) < 8:
            return False, 'Password must be 8 characters or more'
                #ensure password has at least one number
        elif password1.isdigit():
            return False     , 'Password must contain at least one number'    
                #ensure password has at least one special character
        elif password1.isalnum():
            return False, 'Password must contain at least one special character'
                #ensure password has at least one capital letter
        elif password1.islower():
            return ( False, 'Password must contain at least one capital letter')
                #ensure password has at least one lowercase letter
        elif password1.isupper():
        
            return (False  , 'Password must contain at least one lowercase letter')
        else:
            return True, 'Password is valid'