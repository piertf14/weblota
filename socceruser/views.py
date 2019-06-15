#from django.shortcuts import render
from socceruser.models import MyUser
from socceruser.serializers import MyUserSerializer
from rest_framework import generics

# Create your views here.

class MyUserList(generics.ListCreateAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
