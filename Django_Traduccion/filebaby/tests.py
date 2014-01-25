# uploadering/filebaby/tests.py

import os
import hashlib
import tempfile
from contextlib import contextmanager
from mock import Mock, patch

from django.test import RequestFactory
from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from filebaby.context_processors import static_root, media_root
from filebaby.views import FileListView, FileAddView, FileAddHashedView
from filebaby.models import FilebabyFile


@contextmanager
def tempinput(data):
    """Makes a temporary file on drive"""
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(data)
    temp.close()
    yield temp.name
    os.unlink(temp.name)


def setup_view(view, request, *args, **kwargs):
    """Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ``reverse()``

    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


class FileAddViewTest(SimpleTestCase):
    """Test FileAddView class-based view"""
    def setUp(self):
        request = RequestFactory().get(reverse('filebaby-add'))
        view = FileAddView()
        self.view = setup_view(view, request)

    def test_form_valid_saves_form(self):
        """Form is saved when valid"""
        mockform = Mock()
        response = self.view.form_valid(mockform)
        self.assertEqual(response.status_code, 302, "Success redirect needed")
        self.assertTrue(mockform.save.called, "Form must be saved")

    @patch('filebaby.views.messages')
    def test_messages_set(self, mockmessages):
        """Success message set when form valid"""
        mockform = Mock()
        response = self.view.form_valid(mockform)
        self.assertTrue(mockmessages.success.called, "Success msg must be set")


class FileAddHashedViewTest(SimpleTestCase):
    """Test FileAddHashedView class-based view"""
    def setUp(self):
        request = RequestFactory().get(reverse('filebaby-add'))
        view = FileAddHashedView()
        self.file_contents = "NaCl"
        self.expected_md5 = hashlib.md5(self.file_contents).hexdigest()
        self.view = setup_view(view, request)

    def test_form_valid_saves_form(self):
        """Form is saved when valid"""
        # handles form.files.get('f').read()
        modelmock = Mock()
        filemock = Mock()
        filemock.read.return_value = self.file_contents
        mockform = Mock()
        mockform.files.get.return_value = filemock
        mockform.save.return_value = modelmock
        response = self.view.form_valid(mockform)
        self.assertEqual(modelmock.md5, self.expected_md5)
        self.assertTrue(modelmock.save.called, "Model instance must be saved")
        self.assertEqual(response.status_code, 302, "Success redirect needed")
        self.assertTrue(mockform.save.called, "Form must be saved")

    @patch('filebaby.views.messages')
    def test_messages_set(self, mockmessages):
        """Success message set when form valid"""
        filemock = Mock()
        filemock.read.return_value = self.file_contents
        mockform = Mock()
        mockform.files.get.return_value = filemock
        response = self.view.form_valid(mockform)
        self.assertTrue(mockmessages.success.called, "Success msg must be set")


class FilebabyIntegrationTest(TestCase):
    """Tests that URLs make responses"""
    def setUp(self):
        self.client = Client()

    def test_empty_list(self):
        """Get an empty home page"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('No files found' in response.content)

    def test_long_list(self):
        """Get a paginated home page"""
        filename = "./file_{}.txt"
        for x in xrange(10):
            fb = FilebabyFile(f=filename.format(x))
            fb.save()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('pagination' in response.content)
        self.assertEqual(
            len(response.context['files']),
            FileListView.paginate_by)

    def test_add_renders(self):
        """Add file page displays a page with a form"""
        response = self.client.get(reverse('filebaby-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('file_container' in response.content)
        self.assertTrue('input name="f"' in response.content)

    def test_add_file_(self):
        """Test the adding of a file to the view"""
        with tempinput('Test file') as f:
            response = self.client.post(reverse('filebaby-add'), {'f': f})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('messages' in response.context)


class ContextProcessorTest(SimpleTestCase):
    """Test context processor module adds RequestContext variables"""
    @patch('filebaby.context_processors.settings')
    def test_static_root(self, mocksettings):
        """Static root is returned as dictionary"""
        mocksettings.STATIC_ROOT = '/mock/root'
        mockrequest = Mock()
        context = static_root(mockrequest)
        self.assertEqual(context['STATIC_ROOT'], mocksettings.STATIC_ROOT)

    @patch('filebaby.context_processors.settings')
    def test_media_root(self, mocksettings):
        """Media root is returned as dictionary"""
        mocksettings.MEDIA_ROOT = '/mock/root'
        mockrequest = Mock()
        context = media_root(mockrequest)
        self.assertEqual(context['MEDIA_ROOT'], mocksettings.MEDIA_ROOT)
