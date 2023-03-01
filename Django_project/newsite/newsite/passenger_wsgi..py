import os, sys
sys.path.insert(0, '/home/admin1/PycharmProjects/Backend_on_Django/Django_project/newsite')
sys.path.insert(1, '/home/s/slava2sm/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()