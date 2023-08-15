from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search', views.search, name='search'),
    path('api/get-input-values/', views.InputRecordList.as_view(),
         name='api-get-input-values'),
]
