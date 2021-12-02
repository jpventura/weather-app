from graphene_django import DjangoObjectType
import graphene

from weather_app import models
#
#
# class Temperature(DjangoObjectType):
#     class Meta:
#         model = models.Temperature
#         fields = ('id', 'actual', 'date', 'max', 'min')
#
#     actual = graphene.Float(required=True)
#     date = graphene.Date(graphene.Date, required=False)
#     max = graphene.Float(required=True)
#     min = graphene.Float(required=True)


class Weather(DjangoObjectType):
    class Meta:
        model = models.Weather
        fields = ('id', 'city', 'date', 'state', 'lat', 'lon', 'temperatures')

        city = graphene.String(required=True)
        date = graphene.Date(graphene.Date, required=False)
        state = graphene.String(required=True)
        lat = graphene.Float(required=True)
        lon = graphene.Float(required=True)
        temperatures = graphene.List(lambda: Temperature)


class Query(graphene.ObjectType):
    weather = graphene.Field(Weather)
    weathers = graphene.List(Weather)

    temperature = graphene.Field(Weather, name=graphene.ID(required=True))
    # temperatures = graphene.List(Temperature)

    @graphene.resolve_only_args
    def resolve_weather(self, info, id):
        return models.Weather.objects.filter(pk=id)

    @graphene.resolve_only_args
    def resolve_weathers(self, info, **kwargs):
        return models.Weather.objects.all()
    #
    # @graphene.resolve_only_args
    # def resolve_temperature(self, id):
    #     return models.Weather.objects.get(pk=id)
    #
    # @graphene.resolve_only_args
    # def resolve_temperatures(self, info, **kwargs):
    #     return models.Weather.objects.all()

schema = graphene.Schema(query=Query)
