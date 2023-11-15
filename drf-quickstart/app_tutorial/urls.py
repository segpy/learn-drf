from django.urls import path, include
from rest_framework import routers
from app_tutorial import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # App crud urls
    path('', include(router.urls)),
]