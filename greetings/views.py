from django.shortcuts import render
from .models import Person
from .forms import GreetingsForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
 


class PersonCreate(SuccessMessageMixin, CreateView):
    form_class = GreetingsForm
    template_name = 'greetings/person_check.html'
    raise_exception = True


    def form_valid(self, form):
        email = form.cleaned_data['email']
        form.save()
        messages.success(self.request, f'Привіт, {email}')
        return HttpResponseRedirect(self.request.path_info)


class PersonList(ListView):
    model = Person
    template_name = 'greetings/person_list.html'
    context_object_name = 'Persons'