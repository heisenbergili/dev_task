from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Developer
from .forms import DeveloperForm
from django.views.generic import DetailView, ListView


class IndexView(ListView):
    model = Developer
    template_name = 'developer/index.html'
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = DeveloperForm 
        return context

# def index(request):
#     context = {
#          'developers': Developer.objects.all(),
#          'form' : DeveloperForm,
#      }
  
#     return render(request, 'developer/index.html', context)


# The function which add a user that sended by the post request
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


# Detail view of a develper
class DevDetailView(DetailView):
    model = Developer
    template_name = 'developer/detail.html'


# def detail(request, developer_id):
#     developer = get_object_or_404(Developer, pk=developer_id)
#     return render(request, 'developer/detail.html', {'developer': developer})


