from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:todolist_id>/', get_todolist, name='todolist'),
    path('<int:todolist_id>/<int:todo_id>/', update_todo, name='update_todo'),
    path('<int:todolist_id>/<int:todo_id>/delete', delete_todo, name='delete_todo'),
    path('<int:todolist_id>/delete', delete_todolist, name='delete_todolist'),
    path('<int:todolist_id>/<int:todo_id>/done', done_todo, name='done_todo'),
]
