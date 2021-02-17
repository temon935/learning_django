from .models import Task, Workout, Workout_list
from django.forms import ModelForm, TextInput, Textarea, ChoiceField, Select
from django.forms.formsets import formset_factory


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {'title': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите название'
            }),
                    'task': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите описание'
            }),
        }


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['day_of_workout', 'name_of_workout']
        widgets = {'day_of_workout': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите дату тренировки ГГГГ-ММ-ДД'
            }),
                    'name_of_workout': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите название тренировки'
            }),
        }


class WorkoutListForm(ModelForm):
    class Meta:
        model = Workout_list
        fields = ['day_of_workout', 'num_ex', 'name_of_ex', 'weight', 'num_of_repeat', 'numb_of_appr']
        widgets = {'day_of_workout': Select(),
                    'num_ex': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Номер упражнения'
            }),
                    'name_of_ex': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Название упражнения'
            }),
                    'weight': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Вес'
            }),
                    'num_of_repeat': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Количество повторений'
            }),
                    'numb_of_appr': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Номер подхода'
            }),
        }