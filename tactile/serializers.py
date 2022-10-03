from rest_framework import serializers
from .models import textTo

class TactileSerializer(serializers.ModelSerializer):
  class Meta:
    model = textTo
    fields = ['id', 'input']