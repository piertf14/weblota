from rest_framework import serializers
from local.models import Local, CourtSoccer, Gallery


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ('id', 'user', 'slug', 'name', 'description', 'address', 'district_ubigeo',)


class CourtSoccerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourtSoccer
        fields = ('id', 'local', 'slug', 'name', 'description', 'capacity', 'material_type',)


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
