from django.urls import path
from .views import infoDecide


urlpatterns = [
    path('masInfo/', infoDecide)
]
