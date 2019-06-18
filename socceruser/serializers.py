from rest_framework import serializers
from socceruser.models import MyUser


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'dni', 'username', 'first_name', 'last_name', 'password', 'email', 'telephone')
