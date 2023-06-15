from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Room
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.forms import modelform_factory


class WelcomeView(TemplateView):
    template_name = 'meeting/welcome.html'


class ShowRoomView(DetailView):
    model = Room
    template_name = 'meeting/room_detail.html'
    context_object_name = 'detail_room'


class RoomListView(ListView):
    model = Room
    template_name = 'meeting/rooms.html'
    context_object_name = 'rooms'
# todo paginacja i filtracja wolnych pokoi


class CreateRoomView(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'meeting/new.html'
    success_url = '/meeting/rooms/'
    context_object_name = 'form'
