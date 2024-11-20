from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Developer
from .forms import DeveloperForm


def index(request):
    context = {
         'developers': Developer.objects.all(),
         'form' : DeveloperForm,
     }
  
    return render(request, 'developer/index.html', context)

def detail(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})




def add(request):
    form = DeveloperForm(request.POST)

    if form.is_valid():
        Developer.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
    else:
        print("not valid")

    return HttpResponseRedirect(reverse('developer:index'))
