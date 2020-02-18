from django.urls import include, path
from rest_framework import routers
from tutor_match import views


router = routers.DefaultRouter()
router.register(r'api/department', views.DepartmentViewSet)
router.register(r'api/subject', views.SubjectSerializer)
router.register(r'api/schedule', views.ScheduleSerializer)
# router.register(r'/api/tuitionmethod', views.TuitionMethodSerializer)
# router.register(r'/api/tuitionlocation', views.TuitionLocationSerializer)
router.register(r'api/tutor', views.TutorSerializer)
router.register(r'api/student', views.StudentSerializer)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
