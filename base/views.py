from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,DeleteView,CreateView
from .models import Room,Booking,Service
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_users = True

    def get_success_url(self):
        return reverse_lazy('rooms')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('rooms')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('rooms')
        return super(RegisterPage, self).get(*args, **kwargs)


   
class BookingList(ListView):
    model = Booking
    #if u want to add in more data to the the queryset eg :pass color red
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['color']='red'
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
   # context_object_name = 'task'
    success_url = reverse_lazy('your_bookings')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class RoomList(ListView):
    model = Room

class RoomDetail(LoginRequiredMixin, DetailView):
    model = Room
   # template_name='base/task.html'


def rooms_page(request):
	return render(request,'rooms.html')