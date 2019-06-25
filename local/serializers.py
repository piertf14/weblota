from rest_framework import serializers
from local.models import Local, CourtSoccer, Schedule, Gallery

class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ('id', 'name', 'description', 'address', 'district_ubigeo', 'created_at', 'user_id')
