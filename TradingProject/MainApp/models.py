# models.py
from django.db import models
import uuid


class CandleTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
