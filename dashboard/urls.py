from django.conf.urls import patterns, url
from dashboard.views import ContainerListView

urlpatterns = patterns('',
    url(r'^$', ContainerListView.as_view()),
)