{% set class_name = cookiecutter.project_name|title|replace(' ', '') -%}
import logging

from {{ cookiecutter.project_slug }}.config import *

__all__ = [
    '{{ class_name }}',
]

logger = logging.getLogger('{{ cookiecutter.project_slug }}')


# noinspection PyMethodMayBeStatic
class {{ class_name }}(commands.Bot):

    def __init__(self):
        pass
