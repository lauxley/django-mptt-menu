from django import template

from mpttmenu.models import MenuNode

register = template.Library()


@register.inclusion_tag('mpttmenu/menu.html', takes_context=True)
def show_menu(context, obj=None, level_min=0, level_max=None):
    # attempt to find the current object
    # if you are in a detail view, it is recommanded to pass the obj parameter to avoid a useless query
    obj = obj or context.get('object', None) # could be dangerous if object is not used in the default way
    if not obj:
        # is there a better way to do this ? with resolve ?
        l = [m.content_object for m in MenuNode.objects.all() if m.content_object.get_absolute_url() == context['view'].request.path]
        if l:
            obj = l[0]

    return {
        'object': obj,
        'nodes': context['nodes'],
        'level_min': level_min,
        'level_max': level_max,
        }


#def show_breadcrumbs(context):
# a simple recursive tag to fetch the parent
