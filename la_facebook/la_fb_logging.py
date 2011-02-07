import logging
import sys
from django.conf import settings

logger = logging.getLogger("la_fb")


try:
    log_level = settings.FACEBOOK_ACCESS_SETTINGS['LOG_LEVEL']
except (KeyError, AttributeError):
    log_level = 'CRITICAL'

log_level = log_level.upper() #just to catch mistakenly entered lowercase
if hasattr(logging, log_level):
    logger.setLevel(getattr(logging, log_level))

# TODO: should we always log to console, doesn't seem worth another setting
logger.addHandler(logging.StreamHandler(sys.stdout))

try:
    log_file = settings.FACEBOOK_ACCESS_SETTINGS['LOG_FILE']
    logger.addHandler(logging.FileHandler(log_file))
except (KeyError, AttributeError):
    pass
