from rest_framework import serializers
from local.models import Local, CourtSoccer, Gallery, Schedule


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
