from django.db import models

class Feed(models.Model):
    
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.IntegerField(default=0)
    failures = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    

class FeedItem(models.Model):
    
    CONTENT_TYPES = (
        (0, 'plain text'),
        (1, 'html'),
        (2, 'markdown'),    
    )
    
    feed = models.ForeignKey('Feed')
    uid = models.CharField('Unique identifier', max_length=300)
    content = models.TextField()
    content_type = models.IntegerField(choices=CONTENT_TYPES, default=0)
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.uid
        
