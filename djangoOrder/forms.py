from django import forms

class orderForm(forms.Form):
    productID=forms.IntegerField(
        widget=forms.HiddenInput())

    order_Count=forms.IntegerField(
        widget=forms.NumberInput(attrs={"onKeyDown":'return false'}),initial=1,min_value=1)
