from django.contrib import admin
from .models import Name

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = ("name_movie", "pub_date")

admin.site.register(Name, MoviesAdmin)
