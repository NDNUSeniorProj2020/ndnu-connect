from django.urls import include, path
from rest_framework import routers
from tutor_match import views

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'schedule', views.ScheduleViewSet)
# router.register(r'/api/tuitionmethod', views.TuitionMethodSerializer)
# router.register(r'/api/tuitionlocation', views.TuitionLocationSerializer)
router.register(r'tutor', views.TutorViewSet)
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
