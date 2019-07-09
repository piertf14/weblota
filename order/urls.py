from order import views
from django.urls import path

urlpatterns = [
    path('order/', views.OrderAPI.as_view()),
]
