from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Especie)

admin.site.register(Plantacion)
