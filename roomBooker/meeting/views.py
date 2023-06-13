from django.http import HttpResponse
from django.shortcuts import render
from .models import Room


def welcome(request):
    return HttpResponse("fsdiohugwjlcihd")


def showRoom(request):
    rooms = Room.objects.all()
    return render(request, 'meeting/rooms.html', {'rooms': rooms})