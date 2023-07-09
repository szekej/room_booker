from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
    success_url = '/rooms/'
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


class CreateMeetView(LoginRequiredMixin, CreateView):
    model = Meet
    form_class = CreateMeetForm
    template_name = 'meeting/create_meet.html'
    success_url = '/meets'
    context_object_name = 'meet_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meet_form'] = context['form']
        return context

    # Przypisanie obecnie zalogowanego użytkownika do zmiennej user w modelu Meets
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MeetListView(ListView):
    model = Meet
    template_name = 'meeting/meets.html'
    context_object_name = 'meet_list'

    # zwracanie spotkań obecnie zalogowanego użytkownika
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


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
        context['meetings'] = Meet.objects.filter(user=self.request.user)
        return context

