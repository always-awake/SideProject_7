from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'creator',
        'how_many',
        'activate',
    )
