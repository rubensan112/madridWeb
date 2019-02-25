

ACTIVE_ENVIRONMENT = 'dev'
#ACTIVE_ENVIRONMENT = 'prod'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vitadbposgressql',
        'USER': 'admin',
        'PASSWORD': 'alohomora',
        # 'HOST': '172.17.0.1', #Para usarlo el la imagen docker el backend
        'HOST': 'localhost',  # Para usarlo en local el backend
        'PORT': '5432',
    },
}