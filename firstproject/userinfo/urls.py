from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import userinfo




router = DefaultRouter()
router.register('user',userinfo,basename="user")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]