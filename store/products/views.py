from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store-Shop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store-Каталог'
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать!',
        'username': 'Иван иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]
    }
    return render(request, "products/test-context.html", context)