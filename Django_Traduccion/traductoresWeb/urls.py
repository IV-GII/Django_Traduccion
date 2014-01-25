from django.conf.urls import patterns, include, url
from translaters import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'traductoresWeb.views.home', name='home'),
    # url(r'^traductoresWeb/', include('traductoresWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      #url(r'^accounts/profile/', "profile"),
      url(r'^$', views.index, name='index'),
      url(r'^accounts/', include('allauth.account.urls')),
      url(r'^files/', include('filebaby.urls')),
)
