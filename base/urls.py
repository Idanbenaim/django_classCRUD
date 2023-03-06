from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index),
    path('students/',views.manageStudents.as_view()),
]

# from django.urls import path
# from .views import manageStudents
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('students/', manageStudents.as_view(), name='students'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
