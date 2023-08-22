from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register('api/customers', CustomerViewSet, 'customers')

urlpatterns = router.urls