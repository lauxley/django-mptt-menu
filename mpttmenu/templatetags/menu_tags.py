from django import template

from mpttmenu.utils import get_processor_class

register = template.Library()


@register.inclusion_tag('mpttmenu/menu.html', takes_context=True)
def show_menu(context, obj=None, level_min=0, level_max=None):
    cls = get_processor_class()
    proc = cls(context, obj, level_min, level_max)
    return {
        'current': proc.object,
        'nodes': proc.get_nodes()
        }

#def show_breadcrumbs(context):
# a simple recursive tag to fetch the parent
