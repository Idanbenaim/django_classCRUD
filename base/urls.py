from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('index/', views.index),
    path('students/',views.manageStudents.as_view()),
    # path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view()),
]

