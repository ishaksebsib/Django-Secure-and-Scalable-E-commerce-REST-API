from django.shortcuts import render

from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()

    print(query_set[0])
    return render(request, 'hello.html', {'name': 'Mosh'})
