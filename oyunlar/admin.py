from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(ReleaseDate)
admin.site.register(Game)