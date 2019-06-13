from django.db import models
from order import constants as app_constants
from reserve import constants as reserve_constants


class Order(models.Model):
    payment_type = models.IntegerField(
        choices=app_constants.STATUS_CHOICES
    )
    reserve = models.ForeignKey(
        'reserve.Reserve',
        related_name='reserve_order',
        on_delete=models.CASCADE
    )
    status = models.PositiveIntegerField(
        choices=reserve_constants.STATUS_CHOICES,
        default=reserve_constants.STATUS_PENDING
    )
    total = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )