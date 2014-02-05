from django.db import models
from aggregator.models import Feed

class Container(models.Model):
    name = models.CharField(max_length=100)
    modified = models.DateTimeField('modified', auto_now=True)
    order = models.IntegerField('order', unique=True, null=True)
    show_name = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class FeedContainer(Container):
    external_url = models.URLField()
    refreshed = models.DateTimeField('last refresh')
    aggregator = models.ForeignKey(Feed)
    
    def __unicode__(self):
        return self.name
        
class WidgetContainer(Container):
    code = models.TextField()
    # TODO: included in model but not used yet
    include_libs = models.CharField(max_length=50, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
class IFrameContainer(Container):
    url = models.URLField()
    
    def __unicode__(self):
        return self.name
        
class ImageURLContainer(Container):
    url = models.URLField()
    
    def __unicode__(self):
        return self.name
    
class InfoContainer(Container):
    
    def __unicode__(self):
        return self.name

class InfoField(models.Model):
    container = models.ForeignKey(InfoContainer, related_name='fields')
    label = models.CharField(max_length=50)
    text = models.TextField()
    
    def __unicode__(self):
        return self.label
    
    
    