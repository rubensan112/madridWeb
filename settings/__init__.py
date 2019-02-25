try:
    from .local_settings import ACTIVE_ENVIRONMENT

    settings_conf = ACTIVE_ENVIRONMENT
    if ACTIVE_ENVIRONMENT == 'prod':
        from .settings import *
    elif ACTIVE_ENVIRONMENT == 'test':
        from .settings import *
    elif ACTIVE_ENVIRONMENT == 'dev':
        from .settings import *
    print('## SERVER UP ## Using {0} 1settings'.format(settings_conf))
except ImportError:
    print("## SERVER UP ## Using common settings as no environment settings were found")
    from .settings import *

try:
    from .local_settings import *
except ImportError:
    pass

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + FRONTEND_APPS + BACKEND_APPS