from LukeWebsite.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '++j8rg@ybk83g1ewqof7++roq!v)i5xg=ucd#%0nryja!)%m03')
DEBUG = True
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

RIOT_API_KEY = 'RGAPI-5bbe37b9-51da-4c3b-bbd6-dcea99f38e1c'
