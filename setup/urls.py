from django.contrib import admin
from django.urls import path, include
from nossaagua.views import MoradorViewSet, FaltouAguaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('morador', MoradorViewSet, basename='Morador')
router.register('faltouagua', FaltouAguaViewSet, basename= 'FaltouAgua')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]