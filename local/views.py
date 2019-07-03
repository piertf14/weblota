from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from local.models import Local, CourtSoccer
from local.serializers import LocalSerializer, CourtSoccerSerializer, GallerySerializer, CourtSoccerListSerializer
from socceruser.utils import get_access_token


class LocalAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request_data = request.data
        user = get_access_token(request).user
        request_data.update({"user": user.id})
        serializer = LocalSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        user = get_access_token(request).user
        if pk:
            try:
                local = Local.objects.get(pk=pk, user=user)
                serializer = LocalSerializer(local, many=False)
                return Response(serializer.data)
            except Local.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
        locales = user.user_local.all()
        serializer = LocalSerializer(locales, many=True)
        return Response(serializer.data)


class CourtSoccerAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CourtSoccerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        court_soccer = CourtSoccer.objects.all().order_by('-total_reserves')
        if pk:
            try:
                court_soccer = CourtSoccer.objects.get(pk=pk)
                serializer = CourtSoccerListSerializer(court_soccer, many=False)
                return Response(serializer.data)
            except CourtSoccer.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
        serializer = CourtSoccerListSerializer(court_soccer, many=True)
        return Response(serializer.data)


class GalleryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
