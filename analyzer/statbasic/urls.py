from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='hello_analyzer'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
