from django.urls import path
from .views import infoDecide
from .views import infoEgc
from .views import infoTraducciones


urlpatterns = [
    path('masInfo/', infoDecide)
]

urlpatterns = [
    path('masInfoEgc/', infoEgc)
]

urlpatterns = [
    path('masInfoTraducciones/', infoTraducciones)
]

