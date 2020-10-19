from django.contrib.auth import get_user_model
from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import PasswordInput
# check for unique emails & username

not_allowed_usernames = ['abc']

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        widget=PasswordInput(
            attrs={
                "class":"form-control",
                "id": "User-password",
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=PasswordInput(
            attrs={
                "class":"form-control",
                "id": "User-confirm-password",
            }
        )
    )  

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists() or username in not_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another..")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords didn't match.")
        return password2







class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class":"form-control",
                "id": "User-password",
            }
        )
    ) 

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            user = list(qs)[0]
            checkpwd = user.check_password(password)
            print('inside clean--> ', checkpwd)
            if not checkpwd:
                raise forms.ValidationError("Incorrect password.")
        else:
            raise forms.ValidationError("Invalid Credentials, Please try again.")
        
        return {'username': username, 'password': password}

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username__iexact=username)
    #     if not qs.exists():
    #         raise forms.ValidationError("This is not a valid user.")
    #     return username

    # def clean_password(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     qs = User.objects.filter(username__iexact=username)        
    #     if qs.exists():
    #         user = list(qs)[0]
    #         result = user.check_password(password)
    #         if result != True:
    #             raise forms.ValidationError("Incorrect password.")
    #     return password