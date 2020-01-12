from django.contrib import admin
from .models import *


@admin.register(Firma, DHandlowiec, Phandlowy, Tester)
class ViewAdmin(admin.ModelAdmin):
    pass
