from rest_framework.generics import ListCreateAPIView

from cdx.cars.models import Car
from cdx.cars.utils import CarSerializer


class CarView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
