from django.contrib import admin
from .models import Page


# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'permalink', 'update_date')
    list_filter = ('update_date',)
    search_fields = ('title', 'permalink')
    ordering = ('title',)
