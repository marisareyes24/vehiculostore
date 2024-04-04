from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer  #convertir en objetos json 

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer