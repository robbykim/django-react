from .base import *

# Test Runner
TEST_RUNNER = 'snapshottest.django.TestRunner'

# Database
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    # 'default': env.db(),
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MIDDLEWARE.append('myapp.middleware.dev_cors_middleware')
