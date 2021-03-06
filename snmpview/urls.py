from django.conf.urls import patterns, include, url
from snmpview.index.views import index
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snmpview.views.home', name='home'),
    # url(r'^snmpview/', include('snmpview.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^(?P<row_per_page>50|100|500)/$', index),
)
