# -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from mpttmenu.models import MenuNode, SimpleNode
from mpttmenu import default_settings

if 'genericadmin' in settings.INSTALLED_APPS:
    from genericadmin.admin import GenericAdminModelAdmin
else:
    class GenericAdminModelAdmin():
        pass

if 'django_mptt_admin' in settings.INSTALLED_APPS:
    from django_mptt_admin.admin import DjangoMpttAdmin
else:
    class DjangoMpttAdmin():
        pass


class MenuNodeAdmin(GenericAdminModelAdmin, DjangoMpttAdmin, MPTTModelAdmin):
    content_type_whitelist = getattr(settings, 'MENU_ALLOWED_CONTENT_TYPES', default_settings.MENU_ALLOWED_CONTENT_TYPES)

admin.site.register(SimpleNode)
admin.site.register(MenuNode, MenuNodeAdmin)
