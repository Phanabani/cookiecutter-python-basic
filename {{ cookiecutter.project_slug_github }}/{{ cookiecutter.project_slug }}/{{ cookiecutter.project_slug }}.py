{% set class_name = cookiecutter.project_slug|replace("_", " ")|title|replace(" ", "") -%}
import logging

__all__ = ["{{ class_name }}"]

logger = logging.getLogger("{{ cookiecutter.project_slug }}")


# noinspection PyMethodMayBeStatic
class {{ class_name }}:
    def __init__(self):
        pass
