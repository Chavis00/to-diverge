from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
app_name = 'album'
router = DefaultRouter()
router.register(r'', views.AlbumView, basename='album')

urlpatterns = [
    path('', include(router.urls)),
    #path('/create', views.AlbumView.as_view(), name="instances"),

]
