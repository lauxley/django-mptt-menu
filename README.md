Lightweight and modular menu manager using [mptt](http://django-mptt.github.io/django-mptt/) for the [Django](https://www.djangoproject.com) framework.

Usage
=====

Install
-------

* fetch the code

```pip install git+git://github.com/lauxley/django_mptt_menu.git```

* Add mptt and mpttmenu to settings.INSTALLED_APPS

```python
INSTALLED_APPS = (
    [...]
    'mptt',
    'mpttmenu',
    [...]
    )
```

* run a syncdb

```python manage.py syncdb```

* Additionally you can use [django-genericadmin](https://github.com/jschrewe/django-genericadmin)
* And [django-mptt-admin](https://github.com/leukeleu/django-mptt-admin), both improve the admin experience  

* add the {% show_menu %} tag in your base template  
* add a few entries in the admin...  
  
here you go..

Configuration
=============

None of this settings is mandatory.

* MENU_PROCESSOR_CLASS  
  default : 'mpttmenu.processors.MenuProcessor'  
  This is the python path of your menu processor, this is where you will implement all of your logic if you need to change the default behavior (by subclassing processors.MenuProcessor),
  but in most cases using the templatetag options should be enough.  

* MENU_CACHE_BACKEND
  default : 'default'
  If you want to use a specific cache backend for the menu, changes this to its key.

* MENU_CACHE_TIME  
  default : 'default'  
  'default' means to use the default value from the given cache backend;  
  None means forever;  
  Otherwise the value is in seconds.  

* MENU_CACHE_KEY  
  default : 'menu'  
  the key used to store the menu in the cache, change this if you already have a 'menu' key in your cache.

* MENU_ALLOWED_CONTENT_TYPES  
  default : ('mpttmenu/simplenode', )  
  If you choose to use django-genericadmin, this is the list of available content_types for models that can be referenced by the MenuNode. 
  Note that SimpleNode is NOT an abstract model, you don't need to subclass it, it is just the simplest Model to define a menu node (contains a title and an url). 


Advanced usage
==============

Overriding the processor
------------------------

If you need to change the default behavior of the menu you can override the default menu processor to make it show only a part of the tree. 
Of course you could probably put the logic in the template, or even in javascript, but it is a better practice to use the tools that the MenuProcessor offers you,
it means less queries, and a cleaner template code.  
If you do override the processor, don't forget to set MENU_PROCESSOR_CLASS accordingly.

Methods you can override in your own processor: 

* determine_object_from_context  
  Populates the processor instance with the object referenced in the MenuNode, if the object is passed to the templatetag, this method does nothing. 

* determine_node_from_object  
  Populates the processor instance with the node corresponding to the object, if the object has a 'menu_node' attribute (see below), this method will do no query. 

* determine_tree  
  This is were the real logic takes place, depending on the referenced object, this method will return the corresponding part of the menu tree. 
  By default, returns the whole tree. 

* get_default_tree 
  This method is called if no object could be determined (probably on the home page for example), it also returns a part of the menu tree. 
  By default, returns the whole tree. 

There are several convenient methods in the class to help you build the 2 last methods :
> _get_all_nodes  
> _get_root_nodes  
> _get_branch_nodes  
> _get_root_and_branch_nodes  
> _get_chidren_nodes  
> _get_ancestors_nodes  
> _get_root_and_sibblings_nodes  
> _get_root_and_children_nodes  

* get_cache_key 
  Override this if you need to change the cache key  
  By default it returns : ```python 'menu%s' % unicode(self.object or '')```

Optimisation
------------

If you want to make the better of this app you can do two optionals things:

* Pass the referenced object to the show_menu template tag whenever possible, it will avoid the processor to try to guess it.
For example if your menu is made of Sections (a MenuNode will reference a Section), do ```{% show_menu the_current_section %}``` 
In some cases though you won't be able to pass it, if the referenced object is a SimpleNode (used as a static link) for example.

* Add a [reverse generic relation](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#s-reverse-generic-relations) in your models if possible, it will avoid a query.
  ```python
  class MyModel(models.Model):
      [...]
      menu_node = generic.GenericRelation(MenuNode)
  ```
* Also, you can override the template by creating a template with higher precedence in /mpttmenu/menu.html.  
  The default template looks like this:  

```html
{% load mptt_tags %}

<ul>
    {% recursetree nodes %}
        <li {% if current = node.content_object %}class="current"{% elif node.parent and current = node.parent.content_object %}class="current_parent"{% endif %}>
            <a href={{ node.content_object.get_absolute_url }}>{{ node.content_object }}</a>
            <ul class="children">
                {{ children }}
            </ul>
        </li>
    {% endrecursetree %}
</ul>
```

TODO:
=====
* use resolve to determine object for menu if possible
* benchmarks
* get rid of some parenthesis here (they are annoying).
* show_breadcrumbs templatetag
