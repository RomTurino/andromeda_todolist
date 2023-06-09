from django import forms
from .models import PRIORITY, LOW,MEDIUM, HIGH, Todo, Todolist
from typing import Any, Union, Set, Optional, Dict

class PrioritySelect(forms.Select):
    def create_option(self, name: str, value: Any, label: Union[int, str], selected: Union[Set[str], bool], index: int, subindex: Optional[int] = ..., attrs = ...) -> Dict[str, Any]:
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        classes = ['high', 'medium', 'low']
        names = ["#FAA136", "#FFB760", "#FFD8A9"]
        if value:
            option["attrs"]["class"] = classes[value-1]
            option["attrs"]["name"] = names[value-1]
        return option

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "title, todo_date, priority, description".split(', ')
        labels = {
            'title': '',
            'todo_date': '',
            'priority': '',
            'description': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder':'Заголовок дела',
                'class':'item_one_line'
                }),
            'todo_date': forms.DateInput(attrs={
                'placeholder':'дд.мм.гггг',
                'class':'item_one_line',
                'type':'date'
                }),
            'priority': PrioritySelect(attrs={
                'class':'item_priority'
                }),
            'description': forms.Textarea(attrs={
                'placeholder':'Описание',
                'class':'item_description'
                })
        }
    # title = forms.CharField( max_length=64, label='', widget=forms.TextInput(attrs={'placeholder':'Заголовок дела', 'class':'item_one_line'}))
    # todo_date = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder':'дд.мм.гггг', 'class':'item_one_line'}))
    # priority = forms.ChoiceField(label='', choices=PRIORITY, widget=forms.Select(attrs={'class':'item_priority'}))
    # description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Описание','class':'item_description'}))
    


# class TodolistForm(forms.ModelForm):
#     class Meta:
#         model = Todolist
#         fields = ['title']
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'placeholder':'Новый список',
#                 'aria-current':'page',
#                 'id':'todolist'
#                 })
#         }
#         labels = {
#             'title': ''
#         }