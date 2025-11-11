from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
author = {
    'first_name': 'Николай',
    'middle_name': 'Петрович',
    'last_name': 'Сидоров',
    'phone': '8-914-544-20-30',
    'email': 'kolay_sidor12@mail.ru'
}


def home(request):
    text = """
    <h1>Изучаем django</h1>
    <strong>Автор</strong>: <i>Сидоров Н.И.</i>
    """
    return HttpResponse(text)


def about(request):
    html_response = f"""
    Имя: {author['first_name']}<br/>
    Отчество: {author['middle_name']}<br/>
    Фамилия: {author['last_name']}<br/>
    Телефон: {author['phone']}<br/>
    Email: {author['email']}
    """
    return HttpResponse(html_response)


items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"}
]


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


def all_items(request):
    response_html = "<h1>Список товаров</h1><ol>"
    for item in items:
        response_html += f"<li><a href='/item/{item['id']}/'>{item['name']}</a></li>"
    response_html += "</ol>"
    return HttpResponse(response_html)