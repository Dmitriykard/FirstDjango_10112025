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

# Главная страница
def home(request):
    text = """
    <h1>Изучаем django</h1>
    <strong>Автор</strong>: <i>Сидоров Н.И.</i>
    """
    return HttpResponse(text)

# Страница "Обо мне"
def about(request):
    html_response = f"""
    Имя: {author['first_name']}<br/>
    Отчество: {author['middle_name']}<br/>
    Фамилия: {author['last_name']}<br/>
    Телефон: {author['phone']}<br/>
    Email: {author['email']}
    """
    return HttpResponse(html_response)

# Список товаров
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 10},
    {"id": 2, "name": "Куртка кожаная", "quantity": 5},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 15},
    {"id": 4, "name": "Картофель фри", "quantity": 20},
    {"id": 5, "name": "Кепка", "quantity": 8}
]

# Подробности товара по его ID
def item_detail(request, item_id):
    found_item = None
    for item in items:
        if item["id"] == int(item_id):
            found_item = item
            break
    
    if found_item is not None:
        return HttpResponse(
            f"<h1>{found_item['name']}</h1><p><a href='/items/'>Назад к списку товаров</a></p>"
        )
    else:
        return HttpResponse("Товар не найден")

# Список всех товаров
def all_items(request):
    response_html = "<h1>Список товаров</h1><table border='1'><tr><th>Название</th><th>Количество</th></tr>"
    for item in items:
        response_html += f"<tr><td><a href='/item/{item['id']}/'>{item['name']}</a></td><td>{item['quantity']}</td></tr>"
    response_html += "</table>"
    return HttpResponse(response_html)