from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include REST Framework URLs for browsable API
    path('api-auth/', include('rest_framework.urls')),
    # Include our app URLs
    path('', include('Apps.Cuna.urls')),
]
# This file defines the URL patterns for the Django project.
