from django.contrib import admin
from dashboard.models import Container, FeedContainer, InfoContainer, InfoField, WidgetContainer, IFrameContainer

# Register your models here.

class InfoFieldInline(admin.TabularInline):
    model = InfoField
    extra = 3
    
class InfoContainerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'order']}),
    ]
    inlines = [InfoFieldInline]

admin.site.register(Container)
admin.site.register(FeedContainer)
admin.site.register(InfoContainer, InfoContainerAdmin)
admin.site.register(WidgetContainer)
admin.site.register(IFrameContainer)
