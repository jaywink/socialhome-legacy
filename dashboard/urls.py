from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from dashboard.views import ContainerListView

urlpatterns = patterns('',
    url(r'^$', ContainerListView.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)