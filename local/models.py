from django.db import models
from local import constants as app_constants
from local.utils import get_file_path
from socceruser.utils import get_custom_slug


class Local(models.Model):

    user = models.ForeignKey(
        'socceruser.MyUser',
        related_name='user_local',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=225
    )
    slug = models.CharField(
        max_length=225,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=225
    )
    district_ubigeo = models.CharField(
        max_length=15
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def _get_slug(self):
        return get_custom_slug(Local, self.name, instance=self)[:120]

    def save(self, *args, **kwargs):
        self.slug = self._get_slug()
        super(Local, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class CourtSoccer(models.Model):

    local = models.ForeignKey(
        Local,
        related_name='local_court_soccer',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=225
    )
    slug = models.CharField(
        max_length=225,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    capacity = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    material_type = models.PositiveIntegerField(
        choices=app_constants.MATERIAL_TYPES,
        default=app_constants.SYNTHETIC_GRASS
    )
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    total_reserves = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def _get_slug(self):
        return get_custom_slug(Local, self.name, instance=self)[:120]

    def save(self, *args, **kwargs):
        self.slug = self._get_slug()
        super(CourtSoccer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    court_soccer = models.ForeignKey(
        CourtSoccer,
        related_name='court_soccer_schedule',
        on_delete=models.CASCADE
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    duration = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '%s - %s-%s' % (
            self.court_soccer.name, self.start_time, self.end_time)


class Gallery(models.Model):

    court_soccer = models.ForeignKey(
        CourtSoccer,
        related_name='court_soccer_gallery',
        on_delete=models.CASCADE
    )
    photo = models.FileField(
        upload_to=get_file_path
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.court_soccer.name
