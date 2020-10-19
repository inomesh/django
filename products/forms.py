from django import forms

from .models import Products
# class ProductForm(forms.Form):
#     title = forms.CharField()

class ProductForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    class Meta:
        model = Products
        fields = [
            "title",
            "content",
            "price"
        ]
        # exclude = [
        #     # "price"
        # ]

    def clean_title(self):
        data = self.cleaned_data.get("title")
    
        if len(data) < 4:
            raise forms.ValidationError("This is not long enough")
        return data

    def clean_content(self):
        data = self.cleaned_data.get("content")
       
        if len(data) < 4:
            raise forms.ValidationError("This is not long enough")
        return data