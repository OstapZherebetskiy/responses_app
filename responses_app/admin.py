from django.contrib import admin

# Register your models here.
from .models import Areas, Places

admin.site.register(Areas)
admin.site.register(Places)