# -*- coding:utf-8 -*-
from django.core.cache import cache
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from mptt.models import MPTTModel, TreeForeignKey

class MenuNodeManager(models.Manager):
    def get_query_set(self):
        return super(MenuNodeManager, self).get_query_set().filter(active=True)

    def offlines(self):
        return MenuNode.objects.filter(active=False)


class MenuNode(MPTTModel):
    rank = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = MenuNodeManager()

    class MPTTMeta:
        order_insertion_by = ['rank']

    def __unicode__(self):
        return u'%s : %s' % (self.content_type, self.content_object)

    def save(self, *args, **kwargs):
        cache.delete('menu')
        return super(MenuNode, self).save()


class SimpleNode(models.Model):
    """
    The simplest of objects to define a menu node
    """
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=512, unique=True)
    menu_node = generic.GenericRelation(MenuNode)

    def get_absolute_url(self):
        return self.url

    def __unicode__(self):
        return unicode(self.title)
