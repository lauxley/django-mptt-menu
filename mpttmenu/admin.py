# -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from mpttmenu.models import MenuNode, SimpleNode

try:
    from genericadmin.admin import GenericTabularInline
    from genericadmin.admin import GenericAdminModelAdmin as ModelAdmin
except ImportError,e:
    from django.contrib.contenttypes.generic import GenericTabularInline
    from django.contrib.admin import ModelAdmin


class MenuNodeInline(GenericTabularInline):
    model = MenuNode


class MenuNodeAdmin(MPTTModelAdmin, ModelAdmin):
    mptt_level_indent = 20
    inlines = [MenuNodeInline]
    content_type_whitelist = getattr(settings, 'MENU_ALLOWED_CONTENT_TYPES', ('mpttmenu/simplenode', ))

admin.site.register(SimpleNode)
admin.site.register(MenuNode, MenuNodeAdmin)
