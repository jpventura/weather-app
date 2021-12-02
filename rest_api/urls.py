"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Cornershop Weather API')

urlpatterns = [
    # url(r'^', schema_view, name='docs'),
    path('admin/', admin.site.urls),
    path('api/', include('weather_app.urls')),
    url(r'^graphql$', GraphQLView.as_view(graphiql=False)),
    url(r'^graphiql$', GraphQLView.as_view(graphiql=True)),
    url(r'docs', schema_view, name='docs'),
]
