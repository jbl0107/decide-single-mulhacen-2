from django.urls import path
from .views import infoDecide
from .views import infoEgc
from .views import infoTraducciones
from .views import infoJornadas
from .views import infoETSII


urlpatterns = [
    path('masInfo/', infoDecide),
    path('masInfoEgc/', infoEgc),
    path('masInfoTraducciones/', infoTraducciones),
    path('masInfoJornadas/', infoJornadas),
    path('masInfoETSII/' , infoETSII)
]



