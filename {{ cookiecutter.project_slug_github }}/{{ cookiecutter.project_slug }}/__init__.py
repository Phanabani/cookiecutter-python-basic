import logging

from .{{ cookiecutter.project_slug }} import *

__version__ = '{{ cookiecutter.version }}'

logger = logging.getLogger(__name__)
