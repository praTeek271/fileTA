# fileshare/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')

urlpatterns = [
    path('login/', FileViewSet.as_view({'post': 'login'}), name='login'),
    path('', include(router.urls)),
]
