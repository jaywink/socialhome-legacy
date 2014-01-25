from django.views.generic.list import ListView
from django.utils import timezone

from dashboard.models import Container, FeedContainer, InfoContainer

class ContainerListView(ListView):
    
    model = Container

    def get_context_data(self, **kwargs):
        context = super(ContainerListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        # tip from http://stackoverflow.com/a/12357483/1489738
        context['feed_list'] = FeedContainer.objects.all()
        context['info_list'] = InfoContainer.objects.all()
        return context
