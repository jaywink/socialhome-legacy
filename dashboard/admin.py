from django.contrib import admin
from dashboard.models import Container, FeedContainer, InfoContainer, InfoField

# Register your models here.

class InfoFieldInline(admin.TabularInline):
    model = InfoField
    extra = 3
    
class InfoContainerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [InfoFieldInline]

admin.site.register(Container)
admin.site.register(FeedContainer)
admin.site.register(InfoContainer, InfoContainerAdmin)
