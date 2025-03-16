from django.contrib import admin

from .models import Restaurant, Review, SillaUser, SillaProject

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(SillaProject)
admin.site.register(SillaUser)
