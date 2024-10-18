Bootstrap — это популярный фреймворк для разработки адаптивных и мобильных веб-сайтов. Он предоставляет набор инструментов и компонентов, которые позволяют быстро создавать стильные интерфейсы с использованием HTML, CSS и JavaScript. Bootstrap включает в себя систему сеток, готовые стили для кнопок, форм, навигационных панелей и многое другое.
Примеры использования Bootstrap
Система сеток:
Bootstrap использует 12-колоночную сетку, что позволяет легко создавать адаптивные макеты. Например:
```xml
<div class="container">
    <div class="row">
        <div class="col-md-4">Колонка 1</div>
        <div class="col-md-4">Колонка 2</div>
        <div class="col-md-4">Колонка 3</div>
    </div>
</div>
```

Кнопки:
Кнопки можно стилизовать с помощью классов Bootstrap:
```xml
<button type="button" class="btn btn-primary">Основная кнопка</button>
<button type="button" class="btn btn-secondary">Вторичная кнопка</button>
```

Навигационная панель:
Создание адаптивной навигационной панели:
```xml
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Мой сайт</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">Главная</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">О нас</a>
            </li>
        </ul>
    </div>
</nav>
```

Модальные окна:
Использование модальных окон для отображения дополнительной информации:
```xml
<!-- Кнопка для открытия модального окна -->
<button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal">Открыть модальное окно</button>

<!-- Модальное окно -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Модальное окно</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                Содержимое модального окна.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
            </div>
        </div>
    </div>
</div>
```

Заключение
Bootstrap значительно упрощает процесс разработки веб-сайтов, позволяя разработчикам сосредоточиться на функциональности и дизайне, а не на сложностях верстки. С его помощью можно быстро создавать адаптивные и современные интерфейсы.

### Документация: [https://bootstrap-5.ru/docs/5.3/getting-started/introduction/](https://bootstrap-5.ru/docs/5.3/getting-started/introduction/)
