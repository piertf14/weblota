from rest_framework import serializers
from reserve.models import Reserve


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'

    def create(self, validated_data):
        if not Reserve.is_reserved(
                validated_data['reserve_day'],
                validated_data['schedule']):

            reserve = Reserve.objects.create(**{
                'schedule': validated_data['schedule'],
                'user': validated_data['user'],
                'reserve_day': validated_data['reserve_day']
            })
            return reserve
        return None
