from rest_framework import serializers
from .models import CandleTable


class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleTable
        fields = "__all__"
