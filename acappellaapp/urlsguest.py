from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^makeamixdown$', 'acappellaapp.views.makeamixdown', name='makeamixdown'),
    url(r'^findgroup$', 'acappellaapp.views.findgroup', name='findgroup'),
    url(r'^(?P<group_short_code>[^/]+)/$', 'acappellaapp.views.displaygroup', name='displaygroup'),
    url(r'^(?P<group_short_code>[^/]+)/(?P<song_short_code>[^/]+)/$', 'acappellaapp.views.displaysong', name='displaysong'),
    #url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),

   # url(r'^$', TemplateView.as_view(template_name="index.html")),
    #url(r'^arranger/', include('acappellaapp.urlsarranger')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('acappellaapp.urlsguest')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
