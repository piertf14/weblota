from rest_framework import serializers
from order.models import Order
from order.payment import CulqiProcess
from reserve import constants as reserve_constants


class OrderSerializer(serializers.ModelSerializer):
    card_number = serializers.CharField(required=True, max_length=16)
    cvv = serializers.CharField(required=True, max_length=4)
    exp_month = serializers.CharField(required=True, max_length=2)
    exp_year = serializers.CharField(required=True, max_length=4)
    address = serializers.CharField(required=True, max_length=255)
    address_city = serializers.CharField(required=True, max_length=100)
    phone_number = serializers.CharField(required=True, max_length=12)
    product_description = serializers.CharField(required=True, max_length=250)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        process = CulqiProcess()
        status, charge = process.charge(validated_data)
        validated_data.update({
            'status': (reserve_constants.STATUS_PAID
                       if status else reserve_constants.STATUS_FAILED)
        })
        reserve = Order.objects.create(**validated_data)
        return reserve
