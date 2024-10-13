from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_paige(request):
    title: str = "Главная страница "
    text: str = 'Главная страница '
    context = {'title': title,
               'text': text,
               }
    return render(request, "main_paige.html", context)


def second_paige(request):
    title: str = "Вторая страница "
    text_1: str = 'Список 1 '
    text_2: str = 'Список 2 '
    text_3: str = 'Список 3 '
    button_text_1= 'Кнопка_1'
    button_text_2 = 'Кнопка_2'
    button_text_3 = 'Кнопка_3'
    button_text_4 = 'Вернуться на Главную'
    context = {'title': title,
               'text_1': text_1,
               "text_2": text_2,
               "text_3": text_3,
               "button_text_1": button_text_1,
               "button_text_2": button_text_2,
               "button_text_3":button_text_3,
               "button_text_4": button_text_4,

               }
    return render(request, "second_paige.html", context)

def third_paige(request):
    title: str = "Третья Страница "
    text: str = 'Третья страница'
    button_text_1 = 'Вернуться на Главную'
    context = {'title': title,
               'text': text,
               'button_text_1': button_text_1,
               }
    return render(request, "third_paige.html", context)
