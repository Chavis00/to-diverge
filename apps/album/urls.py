from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
app_name = 'album'
router = DefaultRouter()
router.register('', views.AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
]
