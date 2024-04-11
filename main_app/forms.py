from django.forms import ModelForm
from .models import Read, Genre

class ReadForm(ModelForm):
    class Meta:
        model = Read
        fields = ['date', 'activity', 'review']