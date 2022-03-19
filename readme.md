### installing

1. create *virtual enviroments* `virtualenv env`
2. active *virtual enviroments* `source /env/bin/activate`
3. installing dependencies `pip3 install django` plus `pip3 install djangorestframework`
4. create a *django project* `django-admin startproject <project-name>`
> 5. install the *framework* in the *django-project setting file*
> ```python
> ...
> rest_framework
> ```

6. make a app module `./manage.py startapp <app-name>`
7. install the *app module* in *setting.py*
8. **all done!** now we can `import rest_framework`

---

## Serializer

the serializer is a class which return a json whenever the coresponding api is called.
ant the serializer to the reverse too! it get an json and return it to a *django.models.object*.

there is some serializer which doing various things.

1. HyperLinkedModelSerializer

    1.1 this will creat a link for each object from it uniq_id.

2. ModelSerializer

    2.1 will just serialize/deserialize the model.

to use one of thease Serializer, we should import it and then inherit one of theme as
the case setiation.

the *Meta* class will tell the Serializer to user which *model* instance and which one of it`s *fields*.

> Note that we can use `__all__` for all the fields

```python
from rest_framework import serializer
from .models import User


class UserSerializer(serializer.HyperLinkedSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]
```

- an important thing in serializer is **validator**

with validator we can validate the data which User passed to the server.
for example think of we need to check the user hase eough credit to by a product or not.

```python
class DemandSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Demand
        fields = [
            'customer',
            'producer',
            'product',
            'replica'
        ]

    def validate(self, data):
        """
        check the credit of the user,
        check the entity of the product
        """
        
        def validated_data['product'].entity >= validated_data['replica']:
            if validated_data['customer'].amount >= (validated_data['product'].price * validated_data['replica']):
                reise serializer.ValidateErroe('buy credit')
            reise serializer.ValidateError('there is not enough of this product')
        return data
```

- another important thing in seializer is **actions**

actions are used to do something!
in our example we can reduce the cedit amount of the user and reduce the entity of the product

actions are limited to: `list`, `create`, `retrive`, `update`, `destroy`.

```python
# we do create in this example
# when a user requested, and the price and user amount are enough
# and the entity and the replica of the product are anough, this function will run
class DemandSerializer(Serializer.ModelSerializer):
    ...

    def create(self, validated_data):
        user = Customer.objects.get(pk=validated_data['consumer'].pk)
        product_price = validated_data['product'].price
        user.account_amount = user.account_amount - product_price * int(validated_data['replica'])
        user.save()
        return validated_data
```

---

## viewsets

ViewSet are a set of view which represent the data, handel the requests.
in oder to use viewSet we should use of the views, in my case i use *Viewsets.ModelViewSet* which can do all the stuff, like
*list, create, update, etc* and or *'get','post', 'put', 'etc'* if you need to edit the behavior, you can overrider the each of this
actions.

in this case i overide the `create`
to reduce the customer credit amount


```python
from .serializer import DemandSerializer
from .model import Customer
class DemandSerializer(ViewSets.ModelViewset):
    queryset = Demand.object.all()
    serializer_class = DemandSerializer # we use this for all other functions

    def create(self, request):
        serializer_class = DemandSerialzer
        if serializer_class.is_valid():
            final_price = serializer_class.validated_data['product'].price * serializer_class.validate_data['replica']
            user = validate_date['consumer'].id
            user = Customer.object.get(pk=int(user))
            user.account_amout = user.account_amount - final_price
            user.accont_amount.save()
```

## pagination
...

## token
...