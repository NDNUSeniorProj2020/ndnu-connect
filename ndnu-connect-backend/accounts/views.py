from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login as auth_login

from .serializers import UserSerializer, UserSerializerWithToken, RegistrationSerializer, LoginSerializer
from .renderers import UserJSONRenderer
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import AddUserForm


@api_view(['GET'])
def current_user(request):
    # Determine current user by token and return their data
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, req):
        user = req.data.get('user', {})
        serializer = self.serializer_class(data=user)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, req):
        data = req.data.get('user', {})
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, req, *args, **kwargs):
        # Convert user object into a JSON response
        serializer = self.serializer_class(req.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, req, *args, **kwargs):
        serializer_data = req.data.get('user', {})
        serializer = self.serializer_class(req.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserList(APIView):
    # Creates new user
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def signup(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AddUserForm()
    return render(request, 'signup.html', {'form': form})
