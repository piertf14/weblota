from reserve import views
from django.urls import path

urlpatterns = [
    path('reserve/', views.ReserveAPI.as_view()),
]
