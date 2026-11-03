from django.urls import path
from . import views

app_name = 'cine'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pelicula/<int:id>/', views.detalle_pelicula, name='detalle'),
    path('ticket/exito/<int:ticket_id>/', views.exito_ticket, name='exito_ticket'),
]