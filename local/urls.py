from rest_framework.urlpatterns import format_suffix_patterns
from local import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^local$', views.LocalList.as_view()),
    url(r'^local/(?P<pk>[0-9]+)/$', views.LocalDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)