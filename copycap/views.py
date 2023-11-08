from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from copycap.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        new_hello_world = HelloWorld()
        temp = request.POST.get('user_input')
        if temp == 'delete':
            hello_world_list = HelloWorld.objects.all()
            for hello_world in hello_world_list:
                hello_world.delete()
            return HttpResponseRedirect(reverse('copycap:index'))
        else:
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list = HelloWorld.objects.all()
            return HttpResponseRedirect(reverse('copycap:index'))
    else:
        
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'copycap/helloworld.html', context={'hello_world_list': hello_world_list})
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('copycap:index')
    template_name = 'copycap/create.html'
