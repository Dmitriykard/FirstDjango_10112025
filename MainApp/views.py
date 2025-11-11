from django.shortcuts import render
from django.http import HttpResponse

# Авторские данные
author = {
    'first_name': 'Николай',
    'middle_name': 'Петрович',
    'last_name': 'Сидоров',
    'phone': '8-914-544-20-30',
    'email': 'kolay_sidor12@mail.ru'
}

# Список товаров
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 10},
    {"id": 2, "name": "Куртка кожаная", "quantity": 5},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 15},
    {"id": 4, "name": "Картофель фри", "quantity": 20},
    {"id": 5, "name": "Кепка", "quantity": 8}
]

# Главная страница
def home(request):
    text = f"""
    <h1>Изучаем django</h1>
    <strong>Автор</strong>: <i>{author['last_name']} {author['first_name'][0]}.{author['middle_name'][0]}.</i>
    <br><br>
    <a href="/about/">Обо мне</a> | 
    <a href="/items/">Список товаров</a>
    """
    return HttpResponse(text)

# Страница "Обо мне"
def about(request):
    html_response = f"""
    <h2>Обо мне:</h2>
    Имя: {author['first_name']}<br/>
    Отчество: {author['middle_name']}<br/>
    Фамилия: {author['last_name']}<br/>
    Телефон: {author['phone']}<br/>
    Email: {author['email']}<br/><br/>
    <a href="/">На главную</a> | 
    <a href="/items/">Список товаров</a>
    """
    return HttpResponse(html_response)

# Подробности товара по его ID
def item_detail(request, item_id):
    found_item = None
    for item in items:
        if item["id"] == int(item_id):
            found_item = item
            break
    
    if found_item is not None:
        return HttpResponse(
            f"<h1>{found_item['name']}</h1>"
            f"<p>Количество: {found_item['quantity']} шт.</p>"
            f"<p><a href='/items/'>Назад к списку товаров</a></p>"
        )
    else:
        return HttpResponse(
            f"<h3>Товар с id={item_id} не найден</h3>"
            f"<p><a href='/items/'>Назад к списку товаров</a></p>"
        )

# Список всех товаров
def all_items(request):
    response_html = "<h1>Список товаров</h1><ol>"
    for item in items:
        response_html += f"<li><a href='/item/{item['id']}/'>{item['name']}</a> (в наличии: {item['quantity']} шт.)</li>"
    response_html += "</ol>"
    response_html += "<br/><a href='/'>На главную</a> | <a href='/about/'>Обо мне</a>"
    return HttpResponse(response_html)