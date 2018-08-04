#!/usr/bin/env python

#!/usr/bin/env python
import sys
# For deployment add site-package libraries
sys.path.insert(0,'site-package')

import logging
from fixerio_scrape import main
logger = logging.getLogger('fixerio_example')
logger.setLevel(logging.INFO)


def handler(event, context):
    try:
        main.main()
    except Exception as ex:
        msg = 'Unknown exception'
        logger.error("{0} {1}".format(msg, event), exc_info=True)
        sys.exit(2)

