from django.contrib import admin
from .models import Chat

# Register your models here.

@admin.register(Chat)
class chatAdmin(admin.ModelAdmin):
    
    list_display = ["chat_name","chat_admin"]
    list_display_links = ["chat_name"]
    
    search_field = ["chat_name","chat_admin"]
    list_filter = ["chat_name"]
    class Meta:
        model = Chat