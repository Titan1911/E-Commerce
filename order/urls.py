from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('details/', views.details, name='details'),
    path('<int:id>/',views.ordered_items, name='order_details')
]
