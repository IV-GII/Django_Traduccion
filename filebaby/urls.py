from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from filebaby.views import FileListView, FileAddView, FileAddHashedView, FileDownloadView, FileSendView, DeleteFileView, ExtractFileView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uploadering.views.home', name='home'),
    # url(r'^uploadering/', include('uploadering.foo.urls')),
    #
    # This is the view that handles the file uploads
    #url(r'^add/?$', FileAddView.as_view(), name='filebaby-add'),
    #
    # This view hashes uploads to create directories
    url(r'^add$', FileAddHashedView.as_view(), name='filebaby-add'),
    #
    # This view lists uploaded files
    url(r'^$', FileListView.as_view(), name='home'),
#    url(r'^download/(?P<query>\w+)$', FileDownloadView.as_view(), name='home'),
#    url(r'^download/(\?file)(\w{32})$', FileDownloadView.as_view(), name='home'),
    url(r'^download/(.*)', FileDownloadView.as_view(), name='home'),
    url(r'^send/(.*)', FileSendView.as_view(), name='home'),
    url(r'^delete/(.*)', DeleteFileView.as_view(), name='home'),
    url(r'^extract/(.*)', ExtractFileView.as_view(), name='home'),
#    url(r'^download/(\w)$', FileDownloadView.as_view(), name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
