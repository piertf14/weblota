from local import views
from django.urls import path

urlpatterns = [
    path('local/', views.LocalAPI.as_view()),
    path('local/<int:pk>/', views.LocalAPI.as_view()),
    path('court-soccer/', views.CourtSoccerAPI.as_view()),
    path('court-soccer/<int:pk>/', views.CourtSoccerAPI.as_view()),
    path('gallery/', views.GalleryAPI.as_view()),
]