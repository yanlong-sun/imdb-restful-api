from django.urls import path
from browser import views

urlpatterns = [
    path('', views.movieView.as_view()),
    path('<slug:id>/', views.movieDetailView.as_view()),
]
