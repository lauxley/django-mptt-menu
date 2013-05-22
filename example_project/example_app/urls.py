from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView

from .models import ExampleModel

urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=ExampleModel, queryset=ExampleModel.objects.all()), name='example_detail'),
)
