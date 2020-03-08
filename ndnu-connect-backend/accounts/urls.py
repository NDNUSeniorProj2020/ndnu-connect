from django.urls import path

from .views import current_user, UserList, RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view())
]
