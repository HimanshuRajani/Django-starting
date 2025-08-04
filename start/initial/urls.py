from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", initHome, name = 'initHome'),
    path("<int>some.id", some_views, name = 'some')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
