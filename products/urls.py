from django.urls import path
# from .api_views import ProductView, products
from . import views, api_views


urlpatterns = [
    # path('all/',ProductView.as_view()),
    path('', views.show_all, name='products'),
    path('<int:id>', views.detail_view, name='product'),
    path('api', api_views.products),
]

