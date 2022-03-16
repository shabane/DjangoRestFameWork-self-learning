from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProductListView, ProducerListView, CustomerView, DemandView


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('prduct', ProductListView)
router.register('producer', ProducerListView)
router.register('customer', CustomerView)
router.register('demand', DemandView)


urlpatterns = [
    path('', include(router.urls)),
]
