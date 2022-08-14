from LukeWebsite.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '++j8rg@ybk83g1ewqof7++roq!v)i5xg=ucd#%0nryja!)%m03')
DEBUG = os.environ.get('DJANGO_DEBUG', '') == 'True'
# SECURITY WARNING: don't run with debug turned on in production!
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = ['lukepeltier.com']
