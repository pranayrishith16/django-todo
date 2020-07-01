from django.urls import path
from .views import home, delete_todo

urlpatterns = [
    path('', home, name='home'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete'),
]
