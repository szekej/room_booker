from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import classonlymethod, method_decorator
from .models import Room, Meet
from .forms import CreateMeetForm
from django.views.generic import TemplateView, DetailView, ListView, CreateView, DeleteView

from django.forms import modelform_factory


class WelcomeView(TemplateView):
    template_name = 'meeting/welcome.html'


class RoomDetailView(DetailView):
    model = Room
    template_name = 'meeting/room_detail.html'
    context_object_name = 'detail_room'


class RoomListView(ListView):
    model = Room
    template_name = 'meeting/rooms.html'
    context_object_name = 'room_list'


# todo paginacja i filtracja wolnych pokoi


class CreateRoomView(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'meeting/create_room.html'
    success_url = '/meeting/rooms/'
    context_object_name = 'room_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_form'] = context['form']
        return context

    # override default dispatch method to give access only to admin
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DeleteRoomView(DeleteView):
    model = Room
    template_name = 'meeting/delete_room.html'
    success_url = reverse_lazy('rooms')
    context_object_name = 'delete_room'


class CreateMeetView(CreateView):
    model = Meet
    form_class = CreateMeetForm
    template_name = 'meeting/create_meet.html'
    success_url = '/meeting/meets'
    context_object_name = 'meet_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meet_form'] = context['form']
        return context


class MeetListView(ListView):
    model = Meet
    template_name = 'meeting/meets.html'
    context_object_name = 'meet_list'


class MeetDetailView(DetailView):
    model = Meet
    template_name = 'meeting/meet_detail.html'
    context_object_name = 'detail_meet'


class DeleteMeetView(DeleteView):
    model = Meet
    template_name = 'meeting/delete_meet.html'
    success_url = reverse_lazy('meets')
    context_object_name = 'delete_meet'


class WeekPreviewView(TemplateView):
    template_name = 'meeting/week_preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['meet_form'] = context['form']
        return context

