from django.urls import include, path
from rest_framework import routers

from boards import views as boardviews
from job_find import views as jobviews
from tutor_match import views

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'tutor', views.TutorViewSet)
router.register(r'student', views.StudentViewSet)

router.register(r'job', jobviews.JobViewSet)

router.register(r'boards', boardviews.BoardViewSet)
router.register(r'topics', boardviews.TopicViewSet)
router.register(r'posts', boardviews.PostViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
