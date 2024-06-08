from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit_question/', views.submit_question, name='submit_question'),
    path('register/', views.register, name='register'),
    path('community/', views.community, name='community'),
    path('login/', views.user_login, name='login'),
    path('about_us/', views.about_us, name='about_us'),
    path('products/', views.products, name='products'),
    path('doctors_nurses/', views.doctors_nurses, name='doctors_nurses'),
     path('vacancies/', views.vacancies, name='vacancies'),
    path('diabetes_guide/', views.diabetes_guide, name='diabetes_guide'),
    path('heart_disease_guide/', views.heart_disease_guide, name='heart_disease_guide'),
    path('arthritis_guide/', views.arthritis_guide, name='arthritis_guide'),
    path('explore_guide', views.explore_guide, name='explore_guide'),
    path('guides/', views.guides, name='guides'),
     path('nutrition_guide/', views.nutrition_guide, name='nutrition_guide'),
    path('exercise_guide/', views.exercise_guide, name='exercise_guide'),
    path('stress_management_guide/', views.stress_management_guide, name='stress_management_guide'),
]
