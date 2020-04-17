"""ndnuconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

from tutor_match import views as tutorviews
from job_find import views as jobviews
from boards import views as boardviews

router = routers.DefaultRouter()
router.register(r'department', tutorviews.DepartmentViewSet)
router.register(r'subject', tutorviews.SubjectViewSet)
router.register(r'schedule', tutorviews.ScheduleViewSet)
router.register(r'tutor', tutorviews.TutorViewSet)
router.register(r'student', tutorviews.StudentViewSet)

router.register(r'job', jobviews.JobViewSet)
#router.register(r'api/job/<int:pk>', jobviews.JobUpdateAPIView)

router.register(r'board', boardviews.BoardViewSet)
router.register(r'topic', boardviews.TopicViewSet)
router.register(r'post', boardviews.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # View for decoding received JWTs
    path('token-auth/', obtain_jwt_token),

    # URL redirection for Django apps
    path('accounts/', include('accounts.urls')),
    
    path('api/', include(router.urls)),
    path('api/job/<int:pk>/update/',jobviews.JobUpdateView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
