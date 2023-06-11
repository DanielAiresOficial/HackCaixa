"""
HackCaixa URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('resultado/', views.simular_emprestimo, name='resultado'),
]


''' pode usar o seguinte padrão tb.

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resultado/$', views.simular_emprestimo, name='resultado'),
]

'''