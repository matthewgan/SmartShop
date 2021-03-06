from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet


router = DefaultRouter()
router.register(r'', SupplierViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
