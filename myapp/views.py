from django.shortcuts import render, redirect
from datetime import datetime
import random
from .models import Calculation
from .models import Expression
from django.http import HttpResponseBadRequest

def index_page(request):
    context = {
        'author': 'Иван',
        'page_count': 4,
    }
    return render(request, 'index.html', context)

def time_page(request):
    now = datetime.now()
    context = {
        'current_date': now.strftime("%d.%m.%Y"),
        'current_time': now.strftime("%H:%M:%S"),
    }
    return render(request, 'time.html', context)

def calc_page(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    total = a + b

    context = {
        'first_number': a,
        'second_number': b,
        'total': total,
    }
    return render(request, 'calc.html', context)

def home(request):
    return render(request, 'home.html')

def expression(request):
    num_terms = random.randint(2, 4)  # Количество слагаемых от 2 до 4
    terms = [random.randint(10, 99) for _ in range(num_terms)]
    operations = [random.choice(['+', '-']) for _ in range(num_terms - 1)]

    expression_str = str(terms[0])
    for i in range(num_terms - 1):
        expression_str += f" {operations[i]} {terms[i + 1]}"

    result = terms[0]
    for i in range(num_terms - 1):
        if operations[i] == '+':
            result += terms[i + 1]
        else:
            result -= terms[i + 1]

    Calculation.objects.create(expression=expression_str, result=result)
    return render(request, 'expression.html', {'expression': expression_str, 'result': result})

def history(request):
    calculations = Calculation.objects.all()
    return render(request, 'history.html', {'calculations': calculations})

def delete_last_expression(request):
    Expression.objects.last().delete()
    return render(request, 'delete.html', {'message': 'Удалено последнее выражение из истории'})

def clear_all_expressions(request):
    Expression.objects.all().delete()
    return render(request, 'clear.html', {'message': 'История выражений очищена'})

def add_new_expression(request):
    expression = request.GET.get('expression')
    if expression:
        new_expression = Expression(
            content=expression)
        new_expression.save()
        return render(request, 'new.html', {'message': 'Ваше выражение добавлено'})
    return render(request, 'new.html',
                  {'message': 'Пожалуйста, задайте новое выражение с помощью параметра ?expression=ваше_выражение'})