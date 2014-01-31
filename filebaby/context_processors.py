# /uploadering/filebaby/context_processors.py

from django.conf import settings


def static_root(request):
    """
    Adds static-root context variables to the context.

    """
    return {'STATIC_ROOT': settings.STATIC_ROOT}


def media_root(request):
    """
    Adds media-root context variables to the context.

    """
    return {'MEDIA_ROOT': settings.MEDIA_ROOT}
