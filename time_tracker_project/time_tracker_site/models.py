import datetime
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class TimeTracking(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    hours = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    date_created = models.DateTimeField(auto_now_add=True, editable=True)

    def editable(self):
        return timezone.now() - self.date_created < datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'task_id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.author, self.title)
