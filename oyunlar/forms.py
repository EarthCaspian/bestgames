from django.forms import ModelForm
from .models import *

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['oyunTuru', 'oyunPlatformu', 'oyunCikisTarihi', 'oyunIsim', 'oyunAciklama', 'oyunResim']
    
    def __init__(self, *args,**kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
