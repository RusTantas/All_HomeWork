from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_paige(request):
    title: str = "Главная страница "
    text: str = 'Главная страница '
    context = {'title': title,
               'text': text,
               }
    return render(request, "menu.html", context)


def second_paige(request):
    title: str = "Игры "
    list_1: list = ['Atomic Heart', 'Cyberpunk 2077 ','PayDay 2 ' ]

    button_text_1= 'Купить'

    button_text_4 = 'Вернуться на Главную'
    context = {'title': title,

               "button_text_1": button_text_1,

               "button_text_4": button_text_4,
               'list_1':list_1,

               }
    return render(request, "second_paige.html", context)

def third_paige(request):
    title: str = "Третья Страница "
    text: str = 'Третья страница'
    button_text_4 = 'Вернуться на Главную'
    context = {'title': title,
               'text': text,
               'button_text_4': button_text_4,
               }
    return render(request, "third_paige.html", context)
