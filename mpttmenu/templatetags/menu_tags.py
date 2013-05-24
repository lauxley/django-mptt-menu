from django import template

from mpttmenu.utils import get_processor_class

register = template.Library()


@register.inclusion_tag('mpttmenu/menu.html', takes_context=True)
def show_menu(context, *args, **kwargs):
    proc = get_processor_class()(context, *args, **kwargs)
    return {
        'current': proc.object,
        'nodes': proc.get_nodes()
        }

#def show_breadcrumbs(context):
# a simple recursive tag to fetch the parent
