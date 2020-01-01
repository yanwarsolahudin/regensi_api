from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from suppliers.views import SupplierViewSet
from users.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]


# ViewSet Router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns += router.urls
