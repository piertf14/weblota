from rest_framework import serializers
from socceruser.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('dni', 'username', 'first_name', 'last_name', 'password', 'email', 'telephone')
