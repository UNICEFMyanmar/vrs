from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView

from .views import F101List, F101Create, F101Detail, F101Delete, F101Deleted, F101Edit, profile, login_form_page, \
    get_locations, F101CreateOffline, F201Create, F201List, F201Deleted, F201CreateOffline, F201Edit, F201Delete, \
    F201Detail, webapp2_appcache, RHC_choices

urlpatterns = patterns('',
                       url(r'^$', login_form_page, {'template_name': 'page_home.html'}, name='home'),
                       url(r'^about$', login_form_page, {'template_name': 'page_about.html'}, name='dox'),
                       url(r'^accounts/loggedout$', login_form_page, {'template_name': 'registration/logout.html'},
                           name='loggedout'),

                       url(r'^101/add$', permission_required('birth_registration.add_f101')(F101Create.as_view()), name='F101Create'),
                       url(r'^201/add$', permission_required('birth_registration.add_f201')(F201Create.as_view()), name='F201Create'),

                       url(r'^webapp2.appcache$', webapp2_appcache, name='webapp2.appcache'),
                       url(r'^offline$', TemplateView.as_view(template_name='page_home_offline.html'), name="Offline"),
                       url(r'^offline/101/add$', F101CreateOffline.as_view(), name='F101CreateOffline'),
                       url(r'^offline/201/add$', F201CreateOffline.as_view(), name='F201CreateOffline'),
                       url(r'^offline/error$', TemplateView.as_view(template_name='500.html'), name='OfflineError'),


                       url(r'^101/(?P<pk>\d+)$', permission_required('birth_registration.view_f101')(F101Detail.as_view()), name='F101Detail'),
                       url(r'^201/(?P<pk>\d+)$', permission_required('birth_registration.view_f201')(F201Detail.as_view()), name='F201Detail'),

                       url(r'^101/(?P<pk>\d+)/edit$', permission_required('birth_registration.change_f101')(F101Edit.as_view()),
                           name='F101Edit'),
                       url(r'^201/(?P<pk>\d+)/edit$', permission_required('birth_registration.change_f201')(F201Edit.as_view()),
                           name='F201Edit'),


                       url(r'^101/(?P<pk>\d+)/delete$', permission_required('birth_registration.delete_f101')(F101Delete.as_view()),
                           name='F101Delete'),
                       url(r'^201/(?P<pk>\d+)/delete$', permission_required('birth_registration.delete_f201')(F201Delete.as_view()),
                           name='F201Delete'),

                       url(r'^101/(?P<pk>\d+)/restore$', permission_required('birth_registration.delete_f101')(F101Delete.as_view()),
                           name='F101Restore'),
                       url(r'^201/(?P<pk>\d+)/restore$', permission_required('birth_registration.delete_f201')(F201Delete.as_view()),
                           name='F201Restore'),

                       url(r'^101/list$', permission_required('birth_registration.view_f101')(F101List.as_view()), name='F101List'),
                       url(r'^201/list$', permission_required('birth_registration.view_f201')(F201List.as_view()), name='F201List'),

                       url(r'^101/deleted$', permission_required('birth_registration.view_f101')(F101Deleted.as_view()), name='F101Deleted'),
                       url(r'^201/deleted$', permission_required('birth_registration.view_f201')(F201Deleted.as_view()), name='F201Deleted'),

                       url(r'^accounts/profile$', profile, name='profile'),
                       url(r'^accounts/locations.json$', get_locations, name='locations'),

                       url(r'^rhc.json$', permission_required('birth_registration.view_f101')(RHC_choices), name='RHCs'),
)