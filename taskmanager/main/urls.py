from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about-us', views.about, name= 'about'),
    path('create-task', views.create, name= 'create'),
    path('workout', views.workout, name= 'workout'),
    path(r'^create_day/(?P<day>\d+)/', views.create_day, name= 'create_day'),
    path('finance', views.finance, name= 'finance')
]