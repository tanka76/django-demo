
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet
from .views import HelloAPIView,NewAPIView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HelloAPIView.as_view(),name="hello_views"),
    path('new/',NewAPIView.as_view(),name="new_views"),
    path('', include(router.urls)),
]
