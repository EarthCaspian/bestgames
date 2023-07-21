from django.forms import ModelForm
from .models import *
from django.forms import widgets

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['oyunTuru', 'oyunPlatformu', 'oyunCikisTarihi', 'oyunIsim', 'oyunAciklama', 'oyunResim']
        labels = {
            'oyunTuru': 'Game Genre',
            'oyunPlatformu': 'Game Platform',
            'oyunCikisTarihi': 'Release Date',
            'oyunIsim': 'Game Name',
            'oyunAciklama': 'Game Description',
            'oyunResim': 'Game Image',
        }
    
    def __init__(self, *args,**kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        # Change the widget for the release date field to DateInput
        self.fields['oyunCikisTarihi'].widget = widgets.DateInput(attrs={'type': 'date'})