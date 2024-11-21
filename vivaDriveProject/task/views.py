from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Task
from .forms import TaskForm
from developer.models import Developer

class IndexView(ListView): 
    model = Task 
    template_name = "task/index.html"
    context_object_name = 'tasks'
 
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = TaskForm 
        return context 
    
def create(request, developer_id=None):
    developer = None
    if developer_id:
        developer = Developer.objects.get(id=developer_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Utilisation de cleaned_data pour extraire les données manuellement
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            assignee = developer if developer else form.cleaned_data['assignee']
            
            # Créez la tâche avec les données extraites
            Task.objects.create(
                title=title,
                description=description,
                assignee=assignee,
            )
            # Redirigez vers l'index des tâches
            return HttpResponseRedirect(reverse('task:index'))
    else:
        # Si GET, nous créons le formulaire avec le développeur prérempli
        form = TaskForm(initial={'assignee': developer})
        form.fields['assignee'].widget.attrs['disabled'] = 'disabled'

    # Redirection après une requête GET sans traitement du formulaire
    return HttpResponseRedirect(reverse('developer:detail', args=[developer_id]))


def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect(reverse('task:index'))

    return HttpResponseRedirect(reverse('task:index'))
