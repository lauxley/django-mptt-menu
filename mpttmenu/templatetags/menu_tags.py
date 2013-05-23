from django import template
from django.conf import settings

from mpttmenu import default_settings

register = template.Library()


def get_processor_class():
    class_path = getattr(settings, 'MENU_PROCESSOR_CLASS', default_settings.MENU_PROCESSOR_CLASS)
    mod_name, cls_name = class_path.rsplit('.', 1)
    mod = __import__(mod_name, globals(), locals(), [cls_name], -1)
    return getattr(mod, cls_name)


@register.inclusion_tag('mpttmenu/menu.html', takes_context=True)
def show_menu(context, obj=None, level_min=0, level_max=None):
    cls = get_processor_class()
    proc = cls(context, obj, level_min, level_max)
    return {
        'cache_time': getattr(settings, 'MENU_CACHE_TIME', default_settings.MENU_CACHE_TIME),
        'object': proc.object,
        'nodes': proc.get_nodes()
        }

#def show_breadcrumbs(context):
# a simple recursive tag to fetch the parent
