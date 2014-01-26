from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=100)
    modified = models.DateTimeField('modified', auto_now=True)
    order = models.IntegerField('order', unique=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class FeedContainer(Container):
    external_url = models.URLField()
    refreshed = models.DateTimeField('last refresh')
    
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
    
    
    