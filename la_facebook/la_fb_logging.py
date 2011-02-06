import logging
import sys
from django.conf import settings

LOG_FILE = getattr(settings, 'FACEBOOK_LOG_FILE', '/tmp/fb_logging.log')

logger = logging.getLogger("la_fb")
# @@ TODO: get log level from settings
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

logger.addHandler(handler)


