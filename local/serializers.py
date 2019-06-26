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


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('id', 'court_soccer', 'photo', 'created_at')
