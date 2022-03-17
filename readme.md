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


### Serializer

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


### viewsets
...