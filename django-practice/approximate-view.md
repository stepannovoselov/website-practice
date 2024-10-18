Создание проекта и приложения
Создайте проект:
```bash
django-admin startproject myproject
cd myproject
```

Создайте приложение:
```bash
python manage.py startapp myapp
```

Добавьте приложение в settings.py:
```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

Настройка маршрутов
В файле myapp/views.py добавьте следующее:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
```
Затем настройте маршруты в myproject/urls.py:
```python
from django.contrib import admin
from django.urls import path
from myapp.views import home, greet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('greet/<str:name>/', greet),
]
```

Запуск приложения
Запустите сервер с помощью команды:
```bash
python manage.py runserver
```

Перейдите по адресу http://127.0.0.1:8000/ для просмотра результата.

Writing your first Django app: [https://docs.djangoproject.com/en/5.1/intro/tutorial01/](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
