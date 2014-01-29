# /uploadering/filebaby/views.py

import hashlib

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, View, TemplateView
from django.contrib import messages
from django.http import HttpResponse, StreamingHttpResponse

import django
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render_to_response

from filebaby.models import FilebabyFile
from filebaby.forms import FilebabyForm

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

import os
import sys, zipfile, os.path
from django.core.files import File



def deleteFromOS(filepath):
    os.remove(filepath)
    dirpath=os.path.dirname(filepath)
    if dirpath != settings.MEDIA_ROOT and settings.MEDIA_ROOT in dirpath and not os.listdir(dirpath):
        os.rmdir(dirpath)


def extractFile(fileObject, request):
    if fileObject.f.name.endswith(".zip"):
        # Convert file and dir into absolute paths
        fullpath = os.path.join(settings.MEDIA_ROOT,fileObject.f.name)
        dirname = os.path.dirname(settings.MEDIA_ROOT)

        # Get a real Python file handle on the uploaded file
        fullpathhandle = open(fullpath, 'r')

        # Unzip the file, creating subdirectories as needed
        zfobj = zipfile.ZipFile(fullpathhandle)
        for name in zfobj.namelist():
            if name.endswith('/'):
                try: # Don't try to create a directory if exists
                    os.mkdir(os.path.join(dirname, name))
                except:
                    pass
            else:
                outfile = File(open(os.path.join(dirname, name), 'wb+'))
                outfile.write(zfobj.read(name))
                file_o=FilebabyFile(f=name, username=request.user.username, md5=hashlib.md5(outfile.read()).hexdigest())
                file_o.save()
                outfile.close()

        deleteFromOS(fullpath)
        fileObject.delete()
        return True
    return False


class ExtractFileView(TemplateView):
    template_name = "filebaby/index.html"
    def get(self, request, *args, **kwargs):
        extractFile(FilebabyFile.objects.get(md5=request.GET['md5'], id=request.GET['id']), request)
        data={}
#        data={'files': FilebabyFile.objects.all()}
        return render_to_response(self.template_name, data, context_instance=RequestContext(request)) 

class DeleteFileView(TemplateView):
    template_name = "filebaby/index.html"
    def get(self, request, *args, **kwargs):
        data={}
        file_o=FilebabyFile.objects.get(md5=request.GET['md5'], id=request.GET['id'])
        deleteFromOS(file_o.f.path)
        file_o.delete()
        return render_to_response(self.template_name, data, context_instance=RequestContext(request)) 


class FileSendView(TemplateView):
    template_name = "filebaby/index.html"
    def get(self, request, *args, **kwargs):
        data={}
        file_o=FilebabyFile.objects.get(md5=request.GET['md5'])
        message='El usuario ' + request.user.username +'('+ request.user.email +') desea que se traduzca lo siguiente:\n\nFichero ' + file_o.f.name + ": " + request.META['HTTP_HOST'] + "/files/download/?file=" + request.GET['md5']
        send_mail('Fichero' + file_o.f.name, message, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
        file_o.is_sent=is_sent=True
        file_o.save()
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

class FileDownloadView(View):
    def get(self, request, *args, **kwargs):
        try:
            file_o=FilebabyFile.objects.get(md5=request.GET['file'])
        except ObjectDoesNotExist:
            raise Http404
        fsock = open(file_o.f.path, 'r')
        return StreamingHttpResponse (fsock, 'Content-Disposition: attachment; filename="' + file_o.f.path + '"')

class FileListView(ListView):
    model = FilebabyFile
    context_object_name = "files"
    template_name = "filebaby/index.html"
    paginate_by = 20

    def get_queryset(self):
        if self.request.user.is_superuser:
            return FilebabyFile.objects.order_by('-id')
        return FilebabyFile.objects.filter(username=self.request.user.username).order_by('-id')
 
class FileAddView(FormView):
    form_class = FilebabyForm
    success_url = reverse_lazy('home')
    template_name = "filebaby/add.html"
    #template_name = "filebaby/add-boring.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.username = self.request.user.username
        instance.save()
        messages.success(self.request, 'File uploaded!', fail_silently=True)
        return super(FileAddView, self).form_valid(form)


class FileAddHashedView(FormView):
    """This view hashes the file contents using md5"""

    form_class = FilebabyForm
    success_url = reverse_lazy('home')
    template_name = "filebaby/add.html"

    def form_valid(self, form):
        hash_value = hashlib.md5(form.files.get('f').read()).hexdigest()
        # form.save returns a new FilebabyFile as instance
        instance = form.save(commit=False)
        instance.md5 = hash_value
        instance.username = self.request.user.username
        instance.save()

        # descompresion optativa
        if self.request.POST['extractit'] == "yes" and extractFile(instance, self.request):
            messages.success(self.request, 'File uploaded and unziped!', fail_silently=True)

        else:
            messages.success(self.request, 'File uploaded!', fail_silently=True)

        return super(FileAddHashedView, self).form_valid(form)
