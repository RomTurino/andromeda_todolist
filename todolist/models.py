from django.db import models

HIGH = 1
MEDIUM = 2
LOW = 3
PRIORITY = [
        (HIGH, "Высший приоритет"),
        (MEDIUM, "Средний приоритет"),
        (LOW, "Низший приоритет")
    ]

class Todolist(models.Model):
    title = models.CharField(verbose_name='Список дел', max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Списки дел'


class Todo(models.Model):
    
    title = models.CharField(verbose_name='Заголовок дела', max_length=64)
    todo_date = models.DateField(verbose_name="Дата исполнения", null=True, blank=True)
    priority = models.IntegerField(
        choices=PRIORITY,
        default= 1,
        verbose_name="Приоритет",
        null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    fk_todo_todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    complete_date = models.DateField(verbose_name='Дата исполнения', null=True, blank=True)
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ('-complete_date', 'fk_todo_todolist', 'priority', 'todo_date')