# -*- coding: utf-8 -*-
from django.db import models

from model_utils.managers import InheritanceManager


class Container(models.Model):
    name = models.CharField(max_length=100)
    modified = models.DateTimeField('modified', auto_now=True)
    order = models.IntegerField('order', unique=True, null=True)
    show_name = models.BooleanField(default=True)
    
    objects = InheritanceManager()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ["order"]

    
class FeedContainer(Container):
    external_url = models.URLField()
    refreshed = models.DateTimeField('last refresh')
    
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
    CONTENT_TYPES = [
        ("plain", "Plain text (no markup, urlize urls)"),
        ("html", "HTML markup"),
    ]
    
    container = models.ForeignKey(InfoContainer, related_name='fields')
    label = models.CharField(max_length=50)
    text = models.TextField()
    content_type = models.CharField(max_length=30, choices=CONTENT_TYPES, default='plain')
    
    def __unicode__(self):
        return self.label
