from socceruser.models import MyUser
from socceruser.serializers import MyUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class MyUserList(generics.ListCreateAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
	permission_classes = (AllowAny,)


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
	permission_classes = (AllowAny,)

