from local import views
from django.urls import path

urlpatterns = [
    path('local/', views.LocalAPI.as_view()),
    path('court-soccer/', views.CourtSoccerAPI.as_view()),
]