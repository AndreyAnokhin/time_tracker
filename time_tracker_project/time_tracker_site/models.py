from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from decimal import Decimal


class TimeTracking(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    hours = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.author, self.title)
