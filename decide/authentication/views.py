from rest_framework.response import Response
import requests
from rest_framework.status import (
        HTTP_201_CREATED,
        HTTP_400_BAD_REQUEST,
        HTTP_401_UNAUTHORIZED
)
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from base.backends import AuthBackend
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
import requests
from django.urls import reverse
from urllib.parse import quote as q
import oauth2
import secrets
import time
from .serializers import UserSerializer

next = ''

class GetUserView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)
        return Response(UserSerializer(tk.user, many=False).data)


class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})


class RegisterView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)
        if not tk.user.is_superuser:
            return Response({}, status=HTTP_401_UNAUTHORIZED)

        username = request.data.get('username', '')
        pwd = request.data.get('password', '')
        if not username or not pwd:
            return Response({}, status=HTTP_400_BAD_REQUEST)

        try:
            user = User(username=username)
            user.set_password(pwd)
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
        except IntegrityError:
            return Response({}, status=HTTP_400_BAD_REQUEST)
        return Response({'user_pk': user.pk, 'token': token.key}, HTTP_201_CREATED)

def google_login(request):
    redirect_uri = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse("google-login")
    )
    if('code' in request.GET):
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': redirect_uri,
            'client_id': settings.GP_CLIENT_ID,
            'client_secret': settings.GP_CLIENT_SECRET
        }
        url = 'https://accounts.google.com/o/oauth2/token'
        response = requests.post(url, data=params)
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        access_token = response.json().get('access_token')
        response = requests.get(url, params={'access_token': access_token})
        user_data = response.json()
        email = user_data.get('email')
        if email:
            user, _ = User.objects.get_or_create(email=email, username=email)
            data = {
                'first_name': user_data.get('name', '').split()[0],
                'last_name': user_data.get('family_name'),
                'is_active': True
            }
            user.__dict__.update(data)
            user.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
        else:
            messages.error(
                request,
                'Unable to login with Gmail Please try again'
            )
        return redirect(request.GET.get('state', ''))
    else:
        url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=%s"
        scope = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
        scope = " ".join(scope)
        url = url % (settings.GP_CLIENT_ID, scope, redirect_uri, request.GET.get('next'))
        return redirect(url)

def log_in(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request=request, username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', ''))
            else:
                mess = messages.add_message(request, message='Credenciales no válidos', level=0)
                return redirect("/authentication/login2/?next=" + request.GET.get('next', '/'), {'formulario':formulario, 'messages': mess})
    elif request.user.is_authenticated:
        return redirect("/")
    else:
        formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})
    

def log_out(request):
    logout(request)
    return redirect(request.GET.get('next', ''))

def register(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            try:
                usuario = formulario.save()
            except:
                mess = messages.add_message(request, level=0, message='Información inválida')
                return render(request, 'register.html', {'formulario': formulario, 'messages':mess})
            login(request, usuario)
            return redirect(request.GET.get('next', ''))
        else:
            mess = messages.add_message(request, level=0, message='Información inválida')
            return render(request, 'register.html', {'formulario': formulario, 'messages':mess})
    elif request.user.is_authenticated:
        return redirect(request.GET.get('next', ''))
    else:
        formulario = UserCreationForm()
    return render(request, 'register.html', {'formulario': formulario})

def twitter_login(request):
    next_url = request.GET.get('next', '')
    if next_url !='':
        next = next_url
    redirect_uri = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse('twitter-login')
    )
    consumer = oauth2.Consumer(settings.TWITTER_API_ID, settings.TWITTER_API_SECRET)
    token = oauth2.Token(settings.TWITTER_CLIENT_ID, settings.TWITTER_CLIENT_SECRET)
    callbackURI = q(redirect_uri, '')
    req = oauth2.Request.from_consumer_and_token(
        consumer,
        token,
        'POST',
        'https://api.twitter.com/oauth/request_token?oauth_callback=' + callbackURI
    )
    req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer=consumer, token=token)
    response = requests.post(url=req.to_url())
    content = str(response.content)
    contents=content.split('&')
    oauth_token = contents[0].split('=')[1]
    oauth_secret = contents[1].split('=')[1]
    pass