from django.contrib import admin

# Register your models here.

from dashboard.models import Container, FeedContainer, InfoContainer, InfoField

admin.site.register(Container)
admin.site.register(FeedContainer)
admin.site.register(InfoContainer)
admin.site.register(InfoField)