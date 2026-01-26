from django.contrib import admin
from .models import Filme
# Register your models here.
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)
    list_editable = ('preco',)

