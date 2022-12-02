from django.urls import path, include
from . import views

urlpatterns = [
    path('get/', views.getCliente),
    path('post/', views.postCliente),
    path('put/<int:pk>/', views.putCliente),
    path('delete/<int:pk>/', views.deleteCliente)
]
