from socceruser.models import MyUser
from socceruser.serializers import MyUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MyUserList(generics.ListCreateAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
	permission_classes = (AllowAny,)


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
	permission_classes = (AllowAny,)


class MyUserApiView(APIView):
	permission_classes = [AllowAny]

	def post(self, request, format=None):
		serializer = MyUserSerializer(data=request.data)
		if serializer.is_valid():
			myuser = serializer.save()
			myuser.set_password(myuser.password)
			myuser.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
