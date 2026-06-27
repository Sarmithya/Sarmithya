from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('edit/<str:student_id>/', views.edit, name="edit"),
    path('delete/<str:student_id>/', views.delete, name="delete"),
]