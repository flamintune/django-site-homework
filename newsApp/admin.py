from django.contrib import admin
from .models import MyNew

class MyNewAdmin(admin.ModelAdmin):
    style_fields={'description':'ueditor'}

admin.site.register(MyNew, MyNewAdmin)