import os

try:
    ACTIVE_ENVIRONMENT = os.environ['VITA_ENVIRONMENT']
    print("----Using %".format(os.environ['VITA_ENVIRONMENT']))
except:
    ACTIVE_ENVIRONMENT = 'dev'
    print("No environment found. Using dev environment")

try:
    from .settings import *
    settings_conf = ACTIVE_ENVIRONMENT
    if ACTIVE_ENVIRONMENT == 'prod':
        from .settings_prod import *
    elif ACTIVE_ENVIRONMENT == 'test':
        from .settings import *
    elif ACTIVE_ENVIRONMENT == 'dev':
        from .local_settings import *
    print('## SERVER UP ## Using {0} settings'.format(settings_conf))
except ImportError:
    print("## SERVER UP ## Using common settings as no environment settings were found")
    from .settings import *


INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + FRONTEND_APPS + BACKEND_APPS