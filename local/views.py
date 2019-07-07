from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from oauth2_provider.models import AccessToken

from local.models import Local, CourtSoccer, Schedule
from local.serializers import LocalSerializer, CourtSoccerSerializer, GallerySerializer, \
    CourtSoccerListSerializer, ScheduleSerializer
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


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        try:
            get_access_token(request)
            return True
        except:
            if request.method == 'GET':
                return True
        return False


class CourtSoccerAPI(ListAPIView):
    permission_classes = (ReadOnly, )
    serializer_class = CourtSoccerListSerializer
    model = CourtSoccer
    paginate_by = 100

    def post(self, request, format=None):
        serializer = CourtSoccerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def filter(self, queryset):
        duration = self.request.GET.get('duration')
        ubigeo = self.request.GET.get('ubigeo')
        material_type = self.request.GET.get('material_type')
        capacity = self.request.GET.get('capacity')
        if duration:
            course_soccer_id = list(Schedule.objects.filter(
                duration=duration).values_list('court_soccer_id', flat=True))
            queryset = queryset.filter(id__in=course_soccer_id)

        if ubigeo:
            queryset = queryset.filter(local__district_ubigeo__startswith=ubigeo)

        if material_type:
            queryset = queryset.filter(material_type=material_type)

        if material_type:
            queryset = queryset.filter(material_type=material_type)

        if capacity:
            queryset = queryset.filter(material_type=capacity)

        return queryset

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-total_reserves')
        if self.kwargs.get('pk', None):
            court_soccer = CourtSoccer.objects.filter(pk=self.kwargs['pk'])
            return court_soccer

        queryset = self.filter(queryset)
        return queryset

    def put(self, request, pk, format=None):
        try:
            court_soccer = CourtSoccer.objects.get(pk=pk)
            data = request.data
            if data['start_time'] is not None and data['end_time'] is not None:
                court_soccer.start_time = data['start_time']
                court_soccer.end_time = data['end_time']
                court_soccer.save()
                serializer = CourtSoccerSerializer(court_soccer, many=False)
                return Response(serializer.data)
            else:
                return Response({"start_time": 'es requerido', "end_time": 'es requerido'}, status=400)
        except CourtSoccer.DoesNotExist as exe:
            return Response({str(exe)}, status=400)
        except Exception as ex:
            return Response({str(ex)}, status=400)


class GalleryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleAPI(APIView):
    permission_classes = (ReadOnly, )
    def post(self, request, format=None):
        serializer_array = []
        for data_row in request.data:
            serializer = ScheduleSerializer(data=data_row)
            if serializer.is_valid():
                serializer.save()
                serializer_array.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        return Response(serializer_array, status=status.HTTP_201_CREATED)
            

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
