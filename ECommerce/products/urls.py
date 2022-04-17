from django.urls import path
from .api_views import ProductView

urlpatterns = [
    path('all/',ProductView.as_view()),
]
