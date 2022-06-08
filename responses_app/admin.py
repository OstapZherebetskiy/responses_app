from django.contrib import admin

# Register your models here.
from .models import Areas, Places, Comments

admin.site.register(Areas)
admin.site.register(Places)
admin.site.register(Comments)