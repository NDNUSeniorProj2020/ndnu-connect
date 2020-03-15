from django.conf.urls import url
from django.contrib import admin
from .views import home, board_topics


urlpatterns = [
    url('', home, name='boards'),
    url(r'^admin/', admin.site.urls),
    url('<int:pk>/', board_topics, name='boards'),
]