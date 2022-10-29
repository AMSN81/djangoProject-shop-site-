from django import forms

class contactForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"نام و نام خانوادگی"}),max_length=30)

    email=forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"ایمیل"}),max_length=50)

    subject=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"موضوع"}),max_length=30)

    text=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control","rows":"8","placeholder":"متن"}))