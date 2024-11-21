from django import forms

from .models import Task
from developer.models import Developer
 
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee']

    def __init__(self, *args, **kwargs):
        # Récupérer l'assignee si passé dans les kwargs
        developer = kwargs.pop('developer', None)
        super().__init__(*args, **kwargs)

        # Si un développeur est fourni, le définir comme valeur initiale et désactiver le champ
        if developer: 
            self.fields['assignee'].initial = developer
            self.fields['assignee'].widget.attrs['disabled'] = True

   