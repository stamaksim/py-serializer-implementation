from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_car = JSONRenderer().render(serializer.data)
    return serialized_car


def deserialize_car_object(json: bytes) -> Car:
    deserializer = io.BytesIO(json)
    data = JSONParser().parse(deserializer)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    else:
        ValueError("Invalid JSON data for creating Car object.")
