
from django.contrib import admin
from django.urls import path
from .views import HelloAPIView,NewAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HelloAPIView.as_view(),name="hello_views"),
    path('new/',NewAPIView.as_view(),name="new_views")
]
