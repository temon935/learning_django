# Generated by Django 3.1.1 on 2021-01-01 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210101_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='name_of_ex',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='num_ex',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='num_of_repeat',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='numb_of_appr',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='weight',
        ),
        migrations.CreateModel(
            name='Workout_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ex', models.IntegerField(verbose_name='Номер упражнения')),
                ('name_of_ex', models.CharField(max_length=200, verbose_name='Название упражнения')),
                ('weight', models.IntegerField(verbose_name='Вес')),
                ('num_of_repeat', models.IntegerField(verbose_name='Количество повторов')),
                ('numb_of_appr', models.IntegerField(verbose_name='Номер подхода')),
                ('day_of_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.workout')),
            ],
        ),
    ]
