from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from local.models import Local, CourtSoccer, Schedule
from local.serializers import LocalSerializer, CourtSoccerSerializer, GallerySerializer, \
    CourtSoccerListSerializer, ScheduleSerializer, LocalListSerializer, ScheduleListSerializer
from local.utils import ReadOnly
from socceruser.utils import get_access_token


class LocalAPI(APIView):
    permission_classes = (ReadOnly, )

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
                serializer = LocalListSerializer(local, many=False)
                return Response(serializer.data)
            except Local.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
        locales = user.user_local.all()
        serializer = LocalListSerializer(locales, many=True)
        return Response(serializer.data)


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
        data = request.data
        schedule = Schedule.objects.all()

        for i, data_row in enumerate(data):

            for schedule_row in schedule:
                print(schedule_row.start_time)
                print(data_row['start_time'])
                print('-----------------------')
                print(schedule_row.court_soccer_id)
                print(data_row['court_soccer'])
                print('°°°°°°°°°°°°°°°°°°°°°°°°')
                if schedule_row.court_soccer_id == data_row['court_soccer'] and schedule_row.start_time == data_row['start_time']:
                    return Response({"start_time": 'horario no disponible'}, status=400)
                if schedule_row.court_soccer_id == data_row['court_soccer'] and schedule_row.end_time == data_row['end_time']:
                    return Response({"end_time": 'horario no disponible'}, status=400)

            for j, x in enumerate(data):
                if i != j and data_row['start_time'] == x['start_time']:
                    return Response({"start_time": 'horario no disponible'}, status=400)
                if i != j and data_row['end_time'] == x['end_time']:
                    return Response({"end_time": 'horario no disponible'}, status=400)
            serializer = ScheduleSerializer(data=data_row)
            if serializer.is_valid():
                serializer.save()
                serializer_array.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        return Response(serializer_array, status=status.HTTP_201_CREATED)
            
    def get(self, request, court_soccer=None, format=None):
        schedule = Schedule.objects.all()
        serializer_array = []
        if court_soccer:
            try:
                schedule = Schedule.objects.filter(court_soccer_id=court_soccer)
                for i in schedule:
                    serializer = ScheduleListSerializer(i, many=False)
                    serializer_array.append(serializer.data)
                return Response(serializer_array)
            except Schedule.DoesNotExist as exe:
                return Response({str(exe)}, status=400)
        serializer = ScheduleListSerializer(schedule, many=True)
        return Response(serializer.data)    
