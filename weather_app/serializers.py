from rest_framework import serializers
from .models import Weather, Temperature

ISO_DATE_FORMAT = '%Y-%m-%d'

#
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'actual', 'date', 'max', 'min',)

#
# class TemperatureSerializer(serializers.ListSerializer):
#     class Meta:
#         model = Temperature
#         fields = ('id', 'actual', 'date', 'max', 'min',)
#
#     def __init__(self, *args, **kwargs):
#         super(TemperatureSerializer, self).__init__(*args, **kwargs)


TEMPERATURE_MIN = -273.15
TEMPERATURE_MAX = 122.00


class HighScoreSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if type(data) in [int, float, str]:
            data = {'actual': float(data)}

        if 'actual' not in data:
            raise serializers.ValidationError({
                'actual': 'This field is required a temperature.'
            })

        return data

    def to_representation(self, instance):
        return instance.actual

    def create(self, validated_data):
        return Temperature.objects.create(**validated_data)


class TemperatureListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        t = list()
        for i in validated_data:
            t.append(Temperature(**i))
        # temperatures = [Temperature(**temperature) for temperature in validated_data]
        return Temperature.objects.bulk_create(t)


class BookSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = TemperatureListSerializer
        serializer_class = TemperatureSerializer


class WeatherSerializer(serializers.ModelSerializer):
    # temperatures = TemperatureSerializer(many=True)
    # temperatures = serializers.ListSerializer(child=HighScoreSerializer)
    # temperatures = BookSerializer
    # temperatures = serializers.ListField(
    #     child=serializers.IntegerField(min_value=0, max_value=100)
    # )
    temperatures = HighScoreSerializer(many=True)

    class Meta:
        model = Weather
        fields = ('id', 'city', 'date', 'state', 'lat', 'lon', 'temperatures')

    def create(self, validated_data):
        temperatures = validated_data.pop('temperatures')
        weather = Weather.objects.create(**validated_data)

        for t in temperatures:
            Temperature.objects.create(
                weather=weather,
                **WeatherSerializer.format_temperature(t)
            )

        return weather

    @classmethod
    def format_temperature(cls, temperature):
        return {'actual': float(temperature)} if type(temperature) in [int, float, str] else temperature


    @classmethod
    def format_tempera2tures(cls, **kwargs):
        temperatures = map(
            lambda record: {'actual': float(record)} if type(record) in [int, float, str] else record,
            kwargs.pop('temperatures', [])
        )

        return dict(temperatures=temperatures, **kwargs)
