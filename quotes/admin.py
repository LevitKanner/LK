from django.contrib import admin
from .models import Quote


# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'site_status', 'priority')
    list_filter = ('site_status', 'priority', 'submitted')
    search_fields = ('name', 'email')
    ordering = ('-submitted', )
    readonly_fields = ('submitted', )
    fieldsets = (
        (None, {'fields': ('name', 'email', 'description')}),
        ('Contact Information', {
            'classes': ('collapse', ),
            'fields': ('position', 'company', 'address', 'phone', 'web')
        }),
        ('Job Information', {
            'classes': ('collapse', ),
            'fields': ('site_status', 'priority', 'job_file', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse', ),
            'fields': ('quote_date', 'quote_price', 'username')
        })
    )
