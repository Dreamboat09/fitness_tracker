from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileListView.as_view(), name='profile'),
    path('profile/<int:id>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/<int:id>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/<int:id>/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    path('workout/', views.WorkoutListView.as_view(), name='workout'),
    path('workout/<int:id>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('work/create/', views.WorkoutCreateView.as_view(), name='workout_create'),
    path('workout/update/<int:id>/', views.WorkoutUpdateView.as_view(), name='workout_update'),
    path('workout/delete/<int:id>/', views.WorkoutDeleteView.as_view(), name='workout_delete'),
    path('exercise/', views.ExerciseListView.as_view(), name='exercises'),
    path('exercise/<int:id>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
    path('exercise/update/<int:id>/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercise/delete/<int:id>/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
]
