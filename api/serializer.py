from rest_framework import serializers
from .models import User, Products, Producer, Customer, OnDemand
from rest_framework.response import Response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DemandSerializer(serializers.ModelSerializer):
    print('*'*5, 'serializing', '*'*5)
    
    class Meta:
        model = OnDemand
        fields = '__all__'

    def validate(self, data):        
        """
        Check Customer has enough money to but the product or not,
        and check there is enough product or not,
        """
       
        if data['replica'] <= data['product'].entity:
            price = data['product'].price * data['replica']
            amount = data['consumer'].account_amount
            if price > amount:
                raise serializers.ValidationError('you have not enough credit to buy this stuff')
        else:
            raise serializers.ValidationError('there is not enough number of this product')
        return data

    # def create(self, validated_data):
    #     print("fff")
    #     print(validated_data)
    #     user = Customer.objects.get(pk=validated_data['consumer'].pk)
    #     product_price = validated_data['product'].price
    #     print(user.account_amount)
    #     print(product_price)
    #     print(int(validated_data['replica']) * product_price)
    #     user.account_amount = user.account_amount - product_price * int(validated_data['replica'])
    #     user.save()
    #     return validated_data

