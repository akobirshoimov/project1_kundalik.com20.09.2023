from rest_framework.serializers import ModelSerializer
from .models import KundalikModel

class KundalikSerializer(ModelSerializer):
    class Meta:
        model = KundalikModel
        fields = ('__all__')
        