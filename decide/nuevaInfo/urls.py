from django.urls import path
from .views import infoDecide
from .views import infoEgc


urlpatterns = [
    path('masInfo/', infoDecide)
]

urlpatterns = [
    path('masInfoEgc/', infoEgc)
]
