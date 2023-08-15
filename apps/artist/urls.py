from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
app_name = 'artist'
router = DefaultRouter()
router.register('', views.ArtistViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
]
