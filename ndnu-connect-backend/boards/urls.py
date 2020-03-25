from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from django.contrib import admin
from .views import home, board_topics
from boards import views

router = routers.DefaultRouter()
router.register(r'board', views.BoardViewSet)
router.register(r'topic', views.TopicViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    url('', home, name='boards'),
    url(r'^admin/', admin.site.urls),
    url('<int:pk>/', board_topics, name='boards'),
]