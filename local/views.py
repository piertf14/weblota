#from django.shortcuts import render

# Create your views here.

from local.models import Local
from local.serializers import LocalSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

class LocalList(generics.ListCreateAPIView):
	queryset = Local.objects.all()
	serializer_class = LocalSerializer
	permission_classes = (AllowAny,)


class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Local.objects.all()
	serializer_class = LocalSerializer
	permission_classes = (AllowAny,)

