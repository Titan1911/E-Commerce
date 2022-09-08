from django.urls import path
from .api_views import ProductView
from . import views


urlpatterns = [
    # path('all/',ProductView.as_view()),
    path('', views.show_all, name='products'),
    path('<int:id>', views.detail_view, name='product'),
]

