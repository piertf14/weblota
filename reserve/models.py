from django.db import models
from reserve import constants as app_constants


class Reserve(models.Model):
    schedule = models.ForeignKey(
        'local.Schedule',
        related_name='schedule_reserve',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'socceruser.MyUser',
        related_name='user_reserve',
        on_delete=models.CASCADE
    )
    reserve_day = models.DateField()
    status = models.PositiveIntegerField(
        choices=app_constants.STATUS_CHOICES,
        default=app_constants.STATUS_PENDING,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @classmethod
    def is_reserved(cls, day, schedule):
        return cls.objects.filter(
            reserve_day=day,
            schedule=schedule,
            status=app_constants.STATUS_PAID
        ).exists()
