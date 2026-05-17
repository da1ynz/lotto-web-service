from django.urls import path
from . import views

urlpatterns = [
    path('buy/', views.buy_ticket, name='buy_ticket'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('check/', views.check_result, name='check_result'),
    path('admin-draw/', views.admin_draw, name='admin_draw'),
    path('admin-results/', views.admin_results, name='admin_results'),
]