from socceruser import views
from django.urls import path

urlpatterns = [
    path('socceruser/', views.MyUserApiView.as_view()),
    path('socceruser/<int:pk>/', views.MyUserApiView.as_view()),
]