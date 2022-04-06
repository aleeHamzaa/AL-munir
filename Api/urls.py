from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from .views import Productviewset,Product1viewset
router=DefaultRouter()
router.register('Product',Product1viewset,basename='Product')

urlpatterns = [
    path('api/',include(router.urls)),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
