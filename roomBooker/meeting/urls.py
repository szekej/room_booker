from django.urls import path, include
from .views import WelcomeView, ShowRoomView, RoomListView, CreateRoomView


urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('new/', CreateRoomView.as_view(), name='add_room'),
    path('rooms/<int:pk>', ShowRoomView.as_view(), name='room_detail')
]
