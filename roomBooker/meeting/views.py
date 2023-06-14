from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Room
from django.forms import modelform_factory


def welcome(request):
    return HttpResponse("fsdiohugwjlcihd")


def showRoom(request):
    rooms = Room.objects.all()
    return render(request, 'meeting/rooms.html', {'rooms': rooms})


def detail(request, room_id):
    detail_room = get_object_or_404(Room, pk=room_id)
    return render(request, 'meeting/room_detail.html', {'detail_room': detail_room})


FormModel = modelform_factory(Room, exclude=[])


def new(request):
    if request.method == 'POST':
        form = FormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rooms'))
    else:
        form = FormModel
    return render(request, 'meeting/new.html', {'form': form})
