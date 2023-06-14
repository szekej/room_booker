from django.urls import path, include
from .views import welcome, showRoom, new, detail


urlpatterns = [
    path('welcome/', welcome),
    path('rooms/', showRoom, name='rooms'),
    path('new/', new, name='add_room'),
    path('rooms/<int:room_id>', detail, name='room_detail')
]
