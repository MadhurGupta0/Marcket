from django import forms
from . import models

Input_class='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=('name','price','description','image',"quantity")
        widgets={
            'name':forms.TextInput(attrs={'class':Input_class}),
            'price':forms.TextInput(attrs={'class':Input_class}),
            'description':forms.Textarea(attrs={'class':Input_class}),
            'image':forms.FileInput(attrs={'class':Input_class}),
            'quantity':forms.NumberInput(attrs={'class':Input_class})
        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model=models.Item
        fields=('name','price','description','image','quantity')
        widgets={
            'name':forms.TextInput(attrs={'class':Input_class}),
            'price':forms.TextInput(attrs={'class':Input_class}),
            'description':forms.Textarea(attrs={'class':Input_class}),
            'image':forms.FileInput(attrs={'class':Input_class}),
            'quantity': forms.NumberInput(attrs={'class': Input_class})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model= models.ReviewRating
        fields=['subject','rating','review']
        widgets = {
            'subject': forms.TextInput(attrs={'class': Input_class}),
            'rating': forms.Select(attrs={'class': Input_class}),
            'review': forms.TextInput(attrs={'class': Input_class}),

        }

