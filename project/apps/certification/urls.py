from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from .views import F103CreateView, F103ListView, F103DetailView, F103PrintView, F203CreateView, F203DetailView, \
    F203ListView, F203PrintView

urlpatterns = patterns('',
                       # add
                       url(r'^103/add/(?P<f101>\d+)$',
                           permission_required('certification.add_f103')(F103CreateView.as_view()),
                           name='F103CreateView'),
                       url(r'^203/add/(?P<f201>\d+)$',
                           permission_required('certification.add_f203')(F203CreateView.as_view()),
                           name='F203CreateView'),

                       # list
                       url(r'^103/list$',
                           permission_required('certification.view_f103')(F103ListView.as_view()),
                           name='F103ListView'),
                       url(r'^203/list$',
                           permission_required('certification.view_f203')(F203ListView.as_view()),
                           name='F203ListView'),

                       # detail
                       url(r'^103/(?P<pk>\d+)$',
                           permission_required('certification.view_f103')(F103DetailView.as_view()),
                           name='F103DetailView'),
                       url(r'^203/(?P<pk>\d+)$',
                           permission_required('certification.view_f203')(F203DetailView.as_view()),
                           name='F203DetailView'),

                       # print
                       url(r'^103/(?P<pk>\d+)/print$',
                           permission_required('certification.view_f103')(F103PrintView.as_view()),
                           name='F103PrintView'),
                       url(r'^203/(?P<pk>\d+)/print$',
                           permission_required('certification.view_f203')(F203PrintView.as_view()),
                           name='F203PrintView'),

                       )

