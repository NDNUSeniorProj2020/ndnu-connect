from django.urls import path

from .views import current_user, UserList, RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('create-user/', RegistrationAPIView.as_view()),
    path('login-user/', LoginAPIView.as_view())
]
