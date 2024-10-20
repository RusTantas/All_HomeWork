from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.

def sign_up_by_html(request):
    users = ['user_1', 'user_2', 'user_3']
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        age = request.POST.get('age')

        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Password_2: {password_2}")
        print(f"Age: {age}")

        if password_2 != password:
            return HttpResponse('пароль не совпадает')

        if int(age) < 18:
            return HttpResponse('Вы должны быть старше 18 ')

        if username in users:
            return HttpResponse('Пользователь уже существует')

        return HttpResponse(f'Приветсвуем {username}!')

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            users = ['user_1', 'user_2', 'user_3']
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

            return HttpResponse(f'Приветсвуем {username}!')

    else:
        form = ContactForm()
    return render(request, "registration_page.html", {'form': form})

