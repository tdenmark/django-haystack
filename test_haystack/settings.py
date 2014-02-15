import os

SECRET_KEY = "Please do not spew DeprecationWarnings"

# Haystack settings for running tests.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'haystack_tests.db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'haystack',

    'test_haystack.discovery',
    'test_haystack.core',
]

SITE_ID = 1
ROOT_URLCONF = 'test_haystack.core.urls'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'test_haystack.mocks.MockEngine',
    },
    'whoosh': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join('tmp', 'test_whoosh_query'),
        'INCLUDE_SPELLING': True,
    },
    'elasticsearch': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'test_default',
        'INCLUDE_SPELLING': True,
    },
    'simple': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

SITE_ID = 1