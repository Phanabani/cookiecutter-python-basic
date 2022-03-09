import logging
import sys

logger = logging.getLogger('{{ cookiecutter.project_slug }}')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s'
))
logger.addHandler(handler)
