from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import stat, realtime, stat_detail, stat_detail_103

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='map.html'), name="map"),
                       url(r'^stat/(?P<num>[0-9]+)/$', stat, name="stat"),
                       url(r'^stat_detail/(?P<num>[0-9]+)/$', stat_detail, name="stat_detail"),
                       url(r'^stat_detail_103/(?P<num>[0-9]+)/$', stat_detail_103, name="stat_detail_103"),
                       url(r'^realtime/$', realtime, name="realtime"),
                       )
