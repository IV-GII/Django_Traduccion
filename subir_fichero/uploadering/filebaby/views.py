# /uploadering/filebaby/views.py

import hashlib

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages

from filebaby.models import FilebabyFile
from filebaby.forms import FilebabyForm


class RegisterView(FormView):

	form_class = FilebabyForm
    success_url = reverse_lazy('home')
    template_name = "filebaby/add.html"

	def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'SUBIDOO!', fail_silently=True)
        return super(RegisterView, self).form_valid(form)


class FileListView(ListView):

    model = FilebabyFile
    queryset = FilebabyFile.objects.order_by('-id')
    context_object_name = "files"
    template_name = "filebaby/index.html"
    paginate_by = 5


class FileAddView(FormView):

    form_class = FilebabyForm
    success_url = reverse_lazy('home')
    template_name = "filebaby/add.html"
    #template_name = "filebaby/add-boring.html"

    def form_valid(self, form):
        form.save(commit=True)
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
        instance.save()
        messages.success(
            self.request, 'File hashed and uploaded!', fail_silently=True)
        return super(FileAddHashedView, self).form_valid(form)
