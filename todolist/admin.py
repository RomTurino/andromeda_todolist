from django.contrib import admin
from .models import Todolist, Todo

admin.site.register(Todolist)
# admin.site.register(Todo)


@admin.register(Todo)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "todo_date", "priority", "fk_todo_todolist")
    list_filter = ("title", "priority", "fk_todo_todolist")
    search_fields = ("title", )
    fields = ("title", "todo_date", "priority",
              "description", "fk_todo_todolist")



