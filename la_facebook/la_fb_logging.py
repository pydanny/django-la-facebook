import logging
import sys

logger = logging.getLogger("la_fb")
# @@ TODO: get log level from settings
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

logger.addHandler(handler)


