from django.contrib import admin
from .models import event
# Register your models here.
#admin.site.register(event)

@admin.register(event)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 
    'end_date', 'name', 'email', 'photo', 
    'location')
    search_field = ('title', 'name')