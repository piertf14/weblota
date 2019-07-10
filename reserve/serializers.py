from rest_framework import serializers
from reserve.models import Reserve


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'

    def create(self, validated_data):
        return Reserve.objects.create(**validated_data)
