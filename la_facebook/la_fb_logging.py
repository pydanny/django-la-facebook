import logging
import sys
from django.conf import settings

LOG_FILE = getattr(settings, 'FACEBOOK_LOG_FILE', '/tmp/fb_logging.log')

logger = logging.getLogger("la_fb")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

logger.addHandler(handler)


