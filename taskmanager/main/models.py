from django.db import models
import datetime


class Task(models.Model):
    title = models.CharField('Название', max_length= 50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Workout(models.Model):
    day_of_workout = models.DateTimeField('День тренировки')
    name_of_workout = models.CharField('Название тренировки', max_length=200)

    def __str__(self):
        return self.day_of_workout.strftime('%d %B')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class Workout_list(models.Model):
    day_of_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    num_ex = models.IntegerField('Номер упражнения')
    name_of_ex = models.CharField('Название упражнения', max_length=200)
    weight = models.IntegerField('Вес')
    num_of_repeat = models.IntegerField('Количество повторов')
    numb_of_appr = models.IntegerField('Номер подхода')

    def __str__(self):
        return str(self.day_of_workout)

    class Meta:
        verbose_name = 'Тренировочный лист'
        verbose_name_plural = 'Тренировочные листы'


class Finance(models.Model):
    owner = models.CharField('Владелец', max_length=200)
    assets = models.CharField('Активы', max_length=200)
    liabilities = models.CharField('Пассивы', max_length=200)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

