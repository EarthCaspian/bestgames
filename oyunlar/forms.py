from django.forms import ModelForm
from .models import *
from django import forms

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
        # Set a widget for the ManyToManyField oyunPlatformu
        self.fields['oyunPlatformu'].widget = forms.CheckboxSelectMultiple()
        self.fields['oyunPlatformu'].queryset = Platform.objects.all()