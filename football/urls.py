from django.conf.urls import patterns, include, url
from football.views import home,compare1,compare2,results	

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^admin/', include(admin.site.urls)),
	url(r'^compare1/',compare1),url(r'^compare2/',compare2),url(r'^results/',results),
	url(r'',home),

    # Examples:
    # url(r'^$', 'football.views.home', name='home'),
    # url(r'^football/', include('football.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
