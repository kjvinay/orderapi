from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', views.companyView)
router.register('products', views.productView)
router.register('orders', views.orderView)

urlpatterns = [
    path('', include(router.urls))

]
