# Bokeh imports
from bokeh.util.dependencies import import_required

from .apps import DjangoBokehConfig
from .routing import autoload, directory, document

import_required("django", "django is required by bokeh.server.django")
import_required(
    "channels", "The package channels is required by bokeh.server.django and must be installed"
)

default_app_config = "bokeh.server.django.DjangoBokehConfig"
