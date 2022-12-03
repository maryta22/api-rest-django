from django.urls import path, include
from . import views

urlpatterns = [
    path('getCliente/', views.getCliente),
    path('postCliente/', views.postCliente),
    path('putCliente/<int:pk>/', views.putCliente),
    path('deleteCliente/<int:pk>/', views.deleteCliente),
    path('editarSaldo/<int:pk>/<slug:accion>/', views.editarSaldo),
]
