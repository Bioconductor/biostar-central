#
# Django settings for support.bioconductor project.
#   for defaults see  
#   support.bioconductor.org/biostar/settings/base.py
#   this script overrides default settings
#


#
# Load up all known settings
#
from biostar.settings.base import *
import socket
import os

#
# Override settings as needed
#

# Turn off debug mode on deployed servers.

PRODUCTION = socket.gethostname() in ["habu", "support"]

if (PRODUCTION):
    DEBUG = False
else:
    DEBUG = True

# Template debug mode.
TEMPLATE_DEBUG = DEBUG

# Define Categories in top banner
START_CATEGORIES = [
    "Latest", "News", "Jobs", "Tutorials"
]

NAVBAR_TAGS = []

END_CATEGORIES = []

# These are the tags that always show up in the tag recommendation dropdown.
POST_TAG_LIST = NAVBAR_TAGS + ["software error"]

# This will form the navbar
CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES

# This will appear as a top banner.
# It should point to a template that will be included.

TOP_BANNER = ""
#TOP_BANNER = "bioc_banner.html"

# List all extra static paths here.
EXTRA_STATIC = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'static')
]

# Activate the new static path
STATICFILES_DIRS = EXTRA_STATIC + list(STATICFILES_DIRS)


# List all extra template paths here.
EXTRA_TEMPDIR = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'templates')
]

# Activate the new template path
TEMPLATE_DIRS = EXTRA_TEMPDIR + list(TEMPLATE_DIRS)

# Debugging
# This is to show you what the template loading order is:
print("*** Template loading order")
for path in TEMPLATE_DIRS:
    print(path)

# The site logo image on top navigation bar
SITE_LOGO = "bioconductor_logo_rgb_small.jpg"

# How many recent objects to show in the sidebar.
RECENT_VOTE_COUNT = 5
RECENT_USER_COUNT = 5
RECENT_POST_COUNT = 5

# The google id will injected as a template variable.
GOOGLE_TRACKER = "UA-55275703-1"
GOOGLE_DOMAIN = "support.bioconductor.org"

# Define the POSTGRESQL database
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'biostar',
        'USER': 'biostar',
        'PASSWORD': get_env("POSTGRESQL_PASSWORD"),
        'HOST': os.getenv("POSTGRESQL_HOST", "localhost"),
        'PORT': os.getenv("POSTGRESQL_PORT", '5432'),
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is Fa
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", get_env("BIOSTAR_HOSTNAME")]


# Allowed html content.
ALLOWED_TAGS = "p div br code pre h1 h2 h3 h4 h5 h6 hr span s sub sup b i img strong strike em underline super table thead tr th td tbody".split()
ALLOWED_STYLES = 'color font-weight background-color width height'.split()
ALLOWED_ATTRIBUTES = {
    '*': ['class', 'style'],
    'a': ['href', 'rel'],
    'img': ['src', 'alt', 'width', 'height'],
    'table': ['border', 'cellpadding', 'cellspacing'],

}


if 'BIOSTAR_IP' in os.environ:
    ALLOWED_HOSTS.append(os.environ['BIOSTAR_IP'])

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'biostar.wsgi.application'

# These parameters will be inserted into the database automatically.
SITE_NAME = "support.bioconductor.org"

# What domain will handle the replies.
EMAIL_REPLY_PATTERN = "reply+%s+code@bioconductor.org"

# The format of the email that is sent
EMAIL_FROM_PATTERN = u'''"%s [bioc]" <%s>'''

# The subject of the reply goes here
EMAIL_REPLY_SUBJECT = u"[bioc] %s"

# List of callables that know how to import templates from various sources.
if PRODUCTION:
    TEMPLATE_LOADERS = (
       (
            'django.template.loaders.cached.Loader', (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )


# Installed Apps 
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',


    # 'django.contrib.sessions',

    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # The javascript and CSS asset manager.
    'compressor',

    # Enabling the admin and its documentation.
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.sessions',

    # Biostar specific apps.
    'biostar.apps.users',
    'biostar.apps.util',
    'biostar.apps.posts',
    'biostar.apps.messages',
    'biostar.apps.badges',
    'biostar.apps.planet',

    # The main Biostar server.
    'biostar.server',

    # Social login handlers.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.weibo',
 
   # External apps.
    'haystack',
    'crispy_forms',
    'djcelery',
    'kombu.transport.django',
    'south',
    "captcha",
]

# Customize this to match the providers listed in the APPs
SOCIALACCOUNT_PROVIDERS = {

    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': lambda x: 'en_US',
        'PROVIDER_KEY': get_env("FACEBOOK_PROVIDER_KEY"),
        'PROVIDER_SECRET_KEY': get_env("FACEBOOK_PROVIDER_SECRET_KEY"),
    },

    'persona': {
        'REQUEST_PARAMETERS': {'siteName': 'Biostar'}
    },

    'github': {
        'SCOPE': ['email'],
        'PROVIDER_KEY': get_env("GITHUB_PROVIDER_KEY"),
        'PROVIDER_SECRET_KEY': get_env("GITHUB_PROVIDER_SECRET_KEY"),
    },

    'google': {
        'SCOPE': ['email', 'https://www.googleapis.com/auth/userinfo.profile'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'PROVIDER_KEY': get_env("GOOGLE_PROVIDER_KEY"),
        'PROVIDER_SECRET_KEY': get_env("GOOGLE_PROVIDER_SECRET_KEY"),
    },

   'twitter': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'PROVIDER_KEY': get_env("TWITTER_PROVIDER_KEY"),
        'PROVIDER_SECRET_KEY': get_env("TWITTER_PROVIDER_SECRET_KEY"),
    },

     'stackexchange': {
        'SCOPE': ['email'],
        'PROVIDER_KEY': get_env('STACKEXCHANGE_PROVIDER_KEY'),
        'PROVIDER_SECRET': get_env('STACKEXCHANGE_PROVIDER_SECRET_KEY'),
        'KEY': get_env('STACKEXCHANGE_KEY'),
#        'SITE': 'stackoverflow',
    },
}

# Other settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[bioc] "
ACCOUNT_PASSWORD_MIN_LENGHT = 6
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
if ("ON_PRODUCTION" in os.environ and os.environ['ON_PRODUCTION'] == 'True'):
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
else:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"


# Google ReCaptcha No-Captcha settings
# When set the captcha forms will be active.
if "RECAPTCHA_PUBLIC_KEY" in os.environ:
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
else:
    RECAPTCHA_PUBLIC_KEY = ""
if "RECAPTCHA_PRIVATE_KEY" in os.environ:
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
else:
    RECAPTCHA_PRIVATE_KEY = ""
RECAPTCHA_USE_SSL = True  # Defaults to False
NOCAPTCHA = True

# Email
if socket.gethostname() in ["gamay", "habu"] or \
  ("EMAIL_HOST" in os.environ.keys() and \
  (get_env("EMAIL_HOST") == "mailcatcher") \
  or ("amazonaws.com" in get_env("EMAIL_HOST").lower())):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# On deployed servers the following must be set.
EMAIL_HOST = get_env("EMAIL_HOST")
EMAIL_PORT = get_env("EMAIL_PORT", func=int)
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=False
if ("EMAIL_USE_TLS" in os.environ.keys() and \
  get_env("EMAIL_USE_TLS").lower() == "true"):
    EMAIL_USE_TLS=True
