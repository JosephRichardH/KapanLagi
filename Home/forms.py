from django import forms

from .models import Lagu

class PostForm(forms.ModelForm):

    class Meta:
        model = Lagu
        fields = '__all__'
