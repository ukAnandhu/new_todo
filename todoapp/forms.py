from django import forms 
from .models import Task 


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ["name","priority","date"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task name..'}),
            'priority': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter priority..'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['priority'].required = True
        self.fields['date'].required = True
