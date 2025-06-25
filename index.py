import os
from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyDjangoProject.settings")
application = get_wsgi_application()

def handler(request, context):
    return handle(request, application)
