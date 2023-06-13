from django.urls import path, include
from .views import welcome, showRoom


urlpatterns = [
    path('welcome/', welcome),
    path('rooms/', showRoom)
]
