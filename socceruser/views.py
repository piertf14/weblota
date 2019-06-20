from socceruser.models import MyUser
from socceruser.serializers import MyUserSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

	def get(self, request, pk=None, format=None):
		if pk:
			user = self.get_object(pk)
			serializers = MyUserSerializer(user, many=False)
		else:
			users = MyUser.objects.all()
			serializers = MyUserSerializer(users, many=True)
		return Response(serializers.data)

	def get_object(self, pk):
		try:
			return MyUser.objects.get(pk=pk)
		except MyUser.DoesNotExist:
			return None
