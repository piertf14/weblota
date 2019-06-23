from rest_framework import serializers
from local.models import Local, CourtSoccer


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ('id', 'user', 'slug', 'name', 'description', 'address', 'district_ubigeo',)


class CourtSoccerSerializer(serializers.ModelSerializer):
    # local = LocalSerializer()

    class Meta:
        model = CourtSoccer
        fields = ('id', 'local', 'slug', 'name', 'description', 'capacity', 'material_type',)
