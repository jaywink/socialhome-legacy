from django.db import models

# Create your models here.

class Container(models.Model):
    name = models.CharField(max_length=100)
    modified = models.DateTimeField('modified', auto_now=True)
    
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
    container = models.ForeignKey(InfoContainer)
    label = models.CharField(max_length=50)
    text = models.TextField()
    
    def __unicode__(self):
        return self.label
    
    
    