from .models import Account
from rest_framework.serializers import ModelSerializer

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


