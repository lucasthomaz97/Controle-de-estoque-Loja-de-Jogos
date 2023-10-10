from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, alterar, apagar, registrar

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('alterar/<int:id>', alterar, name='alterar'),
    path('apagar/<int:id>', apagar, name='apagar'),
    path('registrar/', registrar, name='registrar')
]