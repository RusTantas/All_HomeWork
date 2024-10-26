from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .models import Buyer, Game


# Create your views here.

def sign_up_by_django(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Buyers = Buyer.objects.all()
            users=[]
            j=0
            for i in Buyers:
                users.append(i.name)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_2 = form.cleaned_data['password_2']
            age = form.cleaned_data['age']
            if password_2 != password:
                return HttpResponse('пароль не совпадает')

            if int(age) < 18:
                return HttpResponse('Вы должны быть старше 18 ')

            if username in users:
                return HttpResponse('Пользователь уже существует')

            return HttpResponse(f'Приветсвуем {username}! у нвс уже есть {users} ')

    else:
        form = ContactForm()
    return render(request, "registration_page.html", {'form': form})

def main_paige(request):
    title_1: str = "Главная страница "
    text: str = 'Главная страница '
    Games = Game.objects.all()
    game = []
    j = 0
    for i in Games:
        game.append(i.title)
    a = 1
    context = {'title': title_1,
               'text': text,
               'Games': Games,
               'a': a,
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
from django.shortcuts import render

# Create your views here.
# Ilya