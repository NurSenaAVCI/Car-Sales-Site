from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.text import slugify
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title','image','description','price','category']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for fieldname in ['title','image','description','price','category']:
                self.fields[fieldname].help_text = None
                self.fields['sent_to'].required = True

        def save(self,*args, **kwargs):
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

        def __str__(self):
            return self.title
