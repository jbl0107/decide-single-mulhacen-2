from django.urls import path
from django.urls import include
from .views import BoothView

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    path('<int:voting_id>/', BoothView.as_view()),
    
]


