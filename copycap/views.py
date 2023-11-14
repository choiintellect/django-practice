from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from copycap.models import UserRealInput, InputG2pk
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from g2pk import G2p
# Create your views here.


def index(request):
    g2p = G2p()
    if request.method == 'POST':
        user_input_list = UserRealInput.objects.all()
        converted_input_list = InputG2pk.objects.all()
        for elements in user_input_list:
            elements.delete()
        for elements in converted_input_list:
            elements.delete()
        new_user_input = UserRealInput()
        temp = request.POST.get('user_input')
        new_user_input.text = temp
        new_user_input.save()
        temp = g2p(temp)
        new_converted_user_input = InputG2pk()
        new_converted_user_input.text = temp
        new_converted_user_input.save()
        return HttpResponseRedirect(reverse('copycap:index'))

    else:
        
        user_input_list = UserRealInput.objects.all()
        converted_input_list = InputG2pk.objects.all()
        return render(request, 'copycap/helloworld.html', context={'user_input_list': user_input_list , 'converted_input_list' : converted_input_list})
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('copycap:index')
    template_name = 'copycap/create.html'
