from django.views.generic.list import ListView
from django.utils import timezone

from dashboard.models import Container

class ContainerListView(ListView):
    
    model = Container
    
    def get_queryset(self):
        return Container.objects.order_by('order')

