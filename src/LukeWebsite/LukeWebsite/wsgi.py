"""
WSGI config for LukeWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

# python_home = '/home/lukep/.virtualenvs/websiteEnv'

# activate_this = python_home + '/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LukeWebsite.settings.prod')

application = get_wsgi_application()
