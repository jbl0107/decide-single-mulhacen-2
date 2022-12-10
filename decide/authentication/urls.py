from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url

from .views import GetUserView, log_out, RegisterView, google_login, log_in, register, twitter_login


urlpatterns = [
    path('login/', obtain_auth_token),
    path('login2/', log_in),
    path('logout/', log_out),
    path('getuser/', GetUserView.as_view()),
    path('register/', register),
    url(r'^google-login/$', view=google_login ,name="google-login"),
    url(r'^twitter-login/$', view=twitter_login, name='twitter-login')
]
