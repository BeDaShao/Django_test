from django.contrib import admin


from links.models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ['code', 'url']
    search_fields = ['code', 'url']
    list_filter = ['code']
    
admin.site.register(Link, LinkAdmin)