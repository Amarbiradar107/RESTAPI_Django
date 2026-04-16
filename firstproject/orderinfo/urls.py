
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import orderinfo


router = DefaultRouter()
router.register('order',orderinfo,basename="order")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]