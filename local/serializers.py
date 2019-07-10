from rest_framework import serializers
from local.models import Local, CourtSoccer, Gallery, Schedule
from reserve import constants as reserve_constants


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ('id', 'user', 'slug', 'name', 'description', 'address', 'district_ubigeo',)


class CourtSoccerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourtSoccer
        fields = ('id', 'local', 'slug', 'name', 'description', 'capacity', 'material_type', 'start_time', 'end_time',)


class CourtSoccerListSerializer(serializers.ModelSerializer):

    local = LocalSerializer()
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = CourtSoccer
        fields = '__all__'

    def get_gallery(self, obj):
        serializer = GallerySerializer(
            obj.court_soccer_gallery.all(), many=True)
        return serializer.data


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = '__all__'

    def get_photo_url(self, obj):
        if obj.photo:
            return obj.photo.url
        return None


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id', 'court_soccer', 'start_time', 'end_time', 'price', 'duration',)


class ScheduleListSerializer(serializers.ModelSerializer):
    is_reserved = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = '__all__'

    def get_is_reserved(self, obj):
        return obj.schedule_reserve.filter(
            status=reserve_constants.STATUS_PAID).exists()


class CourtSoccerLocalSerializer(serializers.ModelSerializer):

    gallery = serializers.SerializerMethodField()

    class Meta:
        model = CourtSoccer
        fields = '__all__'

    def get_gallery(self, obj):
        serializer = GallerySerializer(
            obj.court_soccer_gallery.all(), many=True)
        return serializer.data


class LocalListSerializer(serializers.ModelSerializer):
    court_soccer = serializers.SerializerMethodField()

    def get_court_soccer(self, obj):
        court_soccer = obj.local_court_soccer.all()
        serializer = CourtSoccerLocalSerializer(court_soccer, many=True)
        return serializer.data

    class Meta:
        model = Local
        fields = '__all__'
