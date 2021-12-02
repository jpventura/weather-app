from graphene_django import DjangoObjectType
import graphene

from weather_app import models


class Temperature(DjangoObjectType):
    class Meta:
        model = models.Temperature
        fields = ('id', 'actual', 'date', 'max', 'min')


class Weather(DjangoObjectType):
    class Meta:
        model = models.Weather
        fields = ('id', 'city', 'date', 'state', 'lat', 'lon', 'temperatures')


class Query(graphene.ObjectType):
    weather = graphene.Field(Weather, id=graphene.ID(required=True))
    weathers = graphene.List(Weather)

    temperature = graphene.Field(Weather, name=graphene.String(required=True))
    temperatures = graphene.List(Temperature)

    @graphene.resolve_only_args
    def resolve_weather(self, id):
        return models.Weather.objects.get(pk=id)

    @graphene.resolve_only_args
    def resolve_weathers(self, **kwargs):
        return models.Weather.objects.all()

    @graphene.resolve_only_args
    def resolve_temperature(self, id):
        return models.Weather.objects.get(pk=id)

    @graphene.resolve_only_args
    def resolve_temperatures(self, info, **kwargs):
        return models.Weather.objects.all()

schema = graphene.Schema(query=Query)
