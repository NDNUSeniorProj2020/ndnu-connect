from django.urls import include, path
from rest_framework import routers
from tutor_match import views
from job_find import views as jobviews
from boards import views as boardviews

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'schedule', views.ScheduleViewSet)
# router.register(r'/api/tuitionmethod', views.TuitionMethodSerializer)
# router.register(r'/api/tuitionlocation', views.TuitionLocationSerializer)
router.register(r'tutor', views.TutorViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'job', jobviews.JobViewSet)
router.register(r'board', boardviews.BoardViewSet)
router.register(r'topic', boardviews.TopicViewSet)
router.register(r'post', boardviews.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
