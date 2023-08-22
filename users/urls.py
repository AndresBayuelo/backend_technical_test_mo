from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()

router.register('api-auth', UserViewSet, 'api-auth')

urlpatterns = router.urls