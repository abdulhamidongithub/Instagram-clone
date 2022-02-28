from .models import *
from rest_framework.generics import *
from .serializers import AccountSerializer

class UserCreateList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class UserGDU(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

