from django.forms import ModelForm
from .models import Playtime

class PlaytimeForm(ModelForm):
    class Meta:
        model = Playtime
        fields = ['date', 'petting']
        # we don't need to know "which cat", cause it is already in its detailed form
        