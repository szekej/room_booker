from django.urls import path
from .views import WelcomeView, RoomDetailView, RoomListView,\
    CreateRoomView, DeleteRoomView, CreateMeetView, MeetListView, \
    MeetDetailView, WeekPreviewView


urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('new/', CreateRoomView.as_view(), name='add_room'),
    path('rooms/<int:pk>', RoomDetailView.as_view(), name='room_detail'),
    path('delete/<int:pk>', DeleteRoomView.as_view(), name='delete_room'),
    path('new_meeting/', CreateMeetView.as_view(), name='add_meet'),
    path('meets/', MeetListView.as_view(), name='meets'),
    path('meets/<int:pk>', MeetDetailView.as_view(), name='meet_detail'),
    path('week_preview/', WeekPreviewView.as_view(), name='week_preview'),
]
