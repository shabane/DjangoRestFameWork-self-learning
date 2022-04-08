from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .models import User, Products, Producer, Customer, OnDemand
from .serializer import UserSerializer, ProductSerializer, ProducerSerializer, CustomerSerializer, DemandSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
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
    
    # this will work for all other functions
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 5
    
    def list(self, request, *args, **kwargs):
        # this pagination will just work for this function
        # pagination_class = PageNumberPagination()
        # pagination_class.page_size = 5
        queryset = OnDemand.objects.all()
        serializer_class = DemandSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        print(serializer_class.data)
        return Response(serializer_class.data)

    def create(self, request, *args, **kwargs):
        serializer_class = DemandSerializer(data=request.data)
        if serializer_class.is_valid():
            print("*"*4, serializer_class.validated_data['product'].price) # we should use this instead of quering again.
            print('yes')
            product = Products.objects.get(pk=int(request.data['product']))
            customer = Customer.objects.get(pk=int(request.data['consumer']))
            OnDemand.objects.create(replica=serializer_class.validated_data['replica'], product=product, consumer=customer, producer=serializer_class.validated_data['producer'])
            print('__'*10, serializer_class.validated_data)
            customer.account_amount = customer.account_amount - product.price * int(request.data['replica'])
            product.entity = int(request.data['replica'])
            customer.save()
            product.save()
            print(customer.account_amount)
            res = {
                'msg': 'ok',
                'data': request.data
            }
            return Response(res)
        else:
            print('fuuuuck')
            print(serializer_class.errors)
            res = {
                'msg': 'err',
                'data': serializer_class.errors
            }
            return Response(res)
