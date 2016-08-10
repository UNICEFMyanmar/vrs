from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^', include('birth_registration.urls')),


                       url(r'^grappelli/', include('grappelli.urls')),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^i18n/', include('django.conf.urls.i18n')),

                       url('^accounts/', include('django.contrib.auth.urls')),
                       url(r'^accounts/logout$', 'django.contrib.auth.views.logout',
                           {'next_page': reverse_lazy("loggedout")}),

                       url(r'^select2/', include('django_select2.urls')),
                       url(r'^report_builder/', include('report_builder.urls')),

                       url(r'^favicon\.ico$',
                           RedirectView.as_view(url='/static/favicon.ico')
                       ),

                       )

urlpatterns += patterns('',
                        url(r'^robots.txt$',
                            lambda r: HttpResponse("User-agent: *\nDisallow:\n", content_type="text/plain")
                            )
                        )

if 'map' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^monitor/', include('map.urls'))
                            )

if 'certification' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^', include('certification.urls')),
                            )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^rosetta/', include('rosetta.urls')),
    )


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

js_info_dict = {
    'packages': ('map',),
}

django_info_dict = {
    'domain': 'django',
}

urlpatterns += patterns('',
                        (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict, "js_info_dict"),
                        (r'^jsi18n/django/$', 'django.views.i18n.javascript_catalog', django_info_dict, 'django_info_dict'),
)

handler500 = 'misc.views.custom_500'
handler404 = 'misc.views.custom_404'
