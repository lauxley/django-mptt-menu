from django.core import cache
from django.conf import settings

from mpttmenu import default_settings


def get_processor_class():
    class_path = getattr(settings, 'MENU_PROCESSOR_CLASS', default_settings.MENU_PROCESSOR_CLASS)
    mod_name, cls_name = class_path.rsplit('.', 1)
    mod = __import__(mod_name, globals(), locals(), [cls_name], -1)
    return getattr(mod, cls_name)


class MenuCache(object):
    """
    simple cache helper
    """

    def __init__(self):
        self._backend = self._get_backend()
        self.cache = cache.get_cache(self._backend)
        self._key = self._get_key()
        self._timeout = self._get_timeout()

        self.store = self.cache.get(self._key) or {}

    def __getitem__(self, obj):
        try:
            return self.store[unicode(obj)]
        except KeyError:
            return None

    def __setitem__(self, obj, value):
        self.store[unicode(obj)] = value
        self.cache.set(self._key, self.store, self._timeout)

    def _get_key(self):
        return getattr(settings, 'MENU_CACHE_KEY', default_settings.MENU_CACHE_KEY)

    def _get_backend(self):
        return getattr(settings, 'MENU_CACHE_BACKEND', default_settings.MENU_CACHE_BACKEND)

    def _get_timeout(self):
        t = getattr(settings, 'MENU_CACHE_TIMEOUT', default_settings.MENU_CACHE_TIMEOUT)
        if t == 'default':
            t = self.cache.default_timeout
        return t

    def invalidate(self):
        # log
        self.cache.delete(self._key)
