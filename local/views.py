from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from local.models import Local, CourtSoccer, Schedule
from local.serializers import LocalSerializer, CourtSoccerSerializer, GallerySerializer, CourtSoccerListSerializer, ScheduleSerializer
#, ScheduleListSerializer
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
        locales = user.user_local.all()
        if pk:
            try:
                local = Local.objects.get(pk=pk, user=user)
                serializer = LocalSerializer(local, many=False)
                return Response(serializer.data)
            except Local.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
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
        court_soccer = CourtSoccer.objects.all()
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


class ScheduleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        schedule = Schedule.objects.all()
        if pk:
            try:
                schedule = Schedule.objects.get(pk=pk)
                serializer = ScheduleSerializer(schedule, many=False)
                return Response(serializer.data)
            except Schedule.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)    






'''
    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        if pk:
            horario = self.get_object(pk)
            serializers = ScheduleSerializer(horario, many=False)
        else:
            horarios = Schedule.objects.all()
            serializers = ScheduleSerializer(horarios, many=True)
        return Response(serializers.data)

    def get_object(self, pk):
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            return None
'''




