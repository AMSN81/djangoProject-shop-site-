from django import forms
from django.contrib.auth.models import User

class login_form(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form_control" , "placeholder":"Enter your username" }))
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"Enter your password"}))

class register_form(forms.Form):
    username=forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class":"form_control" , "placeholder":"Enter your username" }))
    email=forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class":"form_control" , "placeholder":"Enter your email" }))
    password=forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"Enter your password" }))

    repassword=forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"Enter your password again" }))


    def clean(self):
        data = self.cleaned_data
        username = self.cleaned_data.get("username")
        print(username)
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("your entered email is used")
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("your entered username is used")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("repassword")
        print(data)
        if password != password2:
            raise forms.ValidationError("Passwords must be the same")
        return data