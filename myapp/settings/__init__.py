import os
import logging

runmode = os.environ.get('RUNMODE', None)
if runmode == 'dev':
    logging.info('Loading DEVELOPMENT environment')
    from .development import *
elif runmode == 'test':
    logging.info('Loading TEST environment')
    from .development import *
elif runmode == 'prod':
    logging.info('Loading PRODUCTION environment')
    from .production import *
else:
    raise ValueError('Invalid value for RUNMODE: %s' % runmode)

