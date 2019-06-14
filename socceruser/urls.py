from rest_framework.urlpatterns import format_suffix_patterns
from socceruser import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^socceruser$', views.MyUserList.as_view()),
    url(r'^socceruser/(?P<pk>[0-9]+)/$', views.MyUserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)