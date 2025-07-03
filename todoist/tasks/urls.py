from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('nova/', views.task_create, name='task_create'),
    path('editar/<int:pk>/', views.task_update, name='task_update'),
    path('excluir/<int:pk>/', views.task_delete, name='task_delete'),
]
