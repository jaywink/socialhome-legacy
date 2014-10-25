from django.views.generic.list import ListView
from django.utils import timezone
from django.conf import settings

from dashboard.models import Container

class ContainerListView(ListView):
    
    model = Container
    
    def get_queryset(self):
        return Container.objects.order_by('order')
        
    def get_context_data(self, **kwargs):
        context = super(ContainerListView, self).get_context_data(**kwargs)
        context['SOCIALHOME_TITLE'] = settings.SOCIALHOME_TITLE
        context['SOCIALHOME_SUBTITLE'] = settings.SOCIALHOME_SUBTITLE
        context['containers'] = Container.objects.all().select_subclasses()
        return context

