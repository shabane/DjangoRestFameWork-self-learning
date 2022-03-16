from rest_framework import viewsets
from rest_framework import generics
from .models import User, Products, Producer, Customer, OnDemand
from .serializer import UserSerializer, ProductSerializer, ProducerSerializer, CustomerSerializer, DemandSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductListView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProducerListView(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DemandView(viewsets.ModelViewSet):
    queryset = OnDemand.objects.all()
    serializer_class = DemandSerializer
