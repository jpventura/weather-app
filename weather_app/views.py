from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from weather_app.models import Weather
from weather_app.serializers import WeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['city', 'date']

    ordering = ['id']
    ordering_fields = ['id', 'date']

    queryset = Weather.objects.all()

    search_fields = ['=city']
    serializer_class = WeatherSerializer
    
    class Meta:
        fields = '__all__'
        model = Weather
