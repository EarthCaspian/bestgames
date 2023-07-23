from django.forms import ModelForm
from .models import *
from django import forms

class GameForm(ModelForm):
    oyunCikisTarihi = forms.DateField(widget=forms.DateInput(format='%d %B, %Y', attrs={'type': 'date'}), label='Game Release Date')
    class Meta:
        model = Game
        fields = ['oyunTuru', 'oyunPlatformu', 'oyunCikisTarihi', 'oyunIsim', 'oyunAciklama', 'oyunResim']
        exclude = ['oyunCikisTarihi']
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

    def save(self, commit=True):
        # get the date input from the form data
        date_input = self.cleaned_data['oyunCikisTarihi']
        # try to find or create a matching ReleaseDate instance
        date_instance, created = ReleaseDate.objects.get_or_create(cikisTarihi=date_input)
        # assign the ReleaseDate instance to the form instance
        self.instance.oyunCikisTarihi = date_instance
        # save the form instance as usual
        return super(GameForm, self).save(commit=commit)