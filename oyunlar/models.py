from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Genre(models.Model):
    tur = models.CharField(max_length=100)

    def __str__(self):
        return self.tur
    
class Platform(models.Model):
    platform = models.CharField(max_length=100)

    def __str__(self):
        return self.platform
    
class ReleaseDate(models.Model):
    cikisTarihi = models.DateField()

    def __str__(self):
        return self.cikisTarihi.strftime('%Y-%m-%d')
    

class Game(models.Model):
    oyunTuru = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    oyunPlatformu = models.ManyToManyField(Platform, blank=True)
    oyunCikisTarihi = models.OneToOneField(ReleaseDate, on_delete=models.SET_NULL, null=True)
    oyunIsim = models.CharField(max_length=100)
    oyunAciklama = RichTextField(max_length=10000)
    oyunResim = models.ImageField(upload_to='oyunlar/')

    def __str__(self):
        return self.oyunIsim
