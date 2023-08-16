from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-description"}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={"class": "form-price"}))
    quantity = forms.IntegerField(min_value=0)
    image = forms.ImageField()