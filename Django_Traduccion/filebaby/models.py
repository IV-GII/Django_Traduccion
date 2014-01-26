# /uploadering/filebaby/models.py

import os
from django.db import models
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django.conf import settings
from django.template import RequestContext


def hashed_uploads_dirs(instance, filename):
    """Returns path with md5 hash as directory"""
    return os.path.join(instance.md5, filename)


class FilebabyFile(models.Model):
    """This holds a single user uploaded file"""
    f = models.FileField(upload_to='.')
    #f = models.FileField(upload_to='%Y/%m/%d')  # Date-based directories
    #f = models.FileField(upload_to=hashed_uploads_dirs)  # Callback defined
    md5 = models.CharField(max_length=32)
