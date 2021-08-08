from LukeWebsite.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '++j8rg@ybk83g1ewqof7++roq!v)i5xg=ucd#%0nryja!)%m03')
DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'read_default_file': os.path.join(BASE_DIR, 'privateSettings', 'db.cnf')
        }
    }
}