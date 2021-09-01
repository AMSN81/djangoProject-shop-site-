from django import forms
from django.contrib.auth.models import User

class login_form(forms.Form):
    username=forms.CharField(
        required=True,
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class":"form_control" , "placeholder":"نام کاربری خود را وارد کنید" }))
    password=forms.CharField(
        required=True,
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"رمز عبور خود را وارد کنید"}))

class register_form(forms.Form):
    username=forms.CharField(
        required=True,
        max_length=20,
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class":"form_control" , "placeholder":"نام کاربری خود را وارد کنید" }))
    email=forms.EmailField(
        required=True,
        max_length=40,
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class":"form_control" , "placeholder":"ایمیل خود را وارد کنید" }))
    password=forms.CharField(
        required=True,
        min_length=8,
        max_length=20,
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"رمز عبور خود را وارد کنید" }))

    repassword=forms.CharField(
        required=True,
        min_length=8,
        max_length=20,
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={"class":"form_control" , "placeholder":"رمز عبور خود را دوباره وارد کنید" }))


    def clean_username(self):
        username = self.cleaned_data.get("username")
        print(username)
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("حسابی با نام کاربری وارد شده از قبل وجود دارد!")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("حسابی با ایمیل استفاده شده از قبل وجود دارد!")
    def clean_repassword(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("repassword")
        if password != password2:
            raise forms.ValidationError("رمز عبور های وارد شده مطاقبت ندارند!")
        return password2