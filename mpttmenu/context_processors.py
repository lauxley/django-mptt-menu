# -*- coding:utf-8 -*-
from mpttmenu.models import MenuNode

def menu(request):
    # get the right MenuNode
    # cache
    return {'nodes': MenuNode.objects.all()}
