from django.shortcuts import render, redirect
from .models import Task, Workout, Workout_list, Finance
from .forms import TaskForm, WorkoutForm, WorkoutListForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout')
        else:
            error = 'Форма была неверной'

    form = WorkoutForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def create_day(request, day):
    error = ''
    if request.method == 'POST':
        form = WorkoutListForm(request.POST)
        if form.is_valid():
            for i in form:
                if i == 'day_of_workout':
                    print('dd')
                    form.save()
        else:
            error = 'Форма была неверной'

    form = WorkoutListForm()
    exercise = Workout_list.objects.all().filter(day_of_workout_id = day)
    context = {
        'form': form,
        'error': error,
        'exercise': exercise
    }
    return render(request, 'main/create_day.html', context)


def workout(request):
    date = Workout.objects.order_by('-id')
    return render(request, 'main/workout.html', {'date': date})


def finance(request):
    tasks = Finance.objects.order_by('-id')
    return render(request, 'main/finance.html', {'title': 'Страница финаносв', 'tasks': tasks})