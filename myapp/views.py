from django.shortcuts import render, redirect
from datetime import datetime
import random
from .models import Calculation
from .models import Expression
from django.contrib import messages

def index_page(request):
    context = {
        'author': 'Иван Вторыгин',
        'page_count': 5,
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
    num_terms = random.randint(2, 4)
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
    last_calculation = Calculation.objects.first()
    if last_calculation:
        last_calculation.delete()
        messages.success(request, "Удалено последнее выражение из истории")
    else:
         messages.warning(request, "История вычислений пуста")
    return redirect('history')


def clear_all_expressions(request):
    if Calculation.objects.exists():
        Calculation.objects.all().delete()
        messages.success(request, "История выражений очищена")
    else:
        messages.warning(request, "История вычислений пуста")
    return redirect('history')

def add_new_expression(request):
    message = ""
    expression = request.GET.get('expression')
    result = request.GET.get('result')
    if expression and result:
        try:
            result = float(result)
            Calculation.objects.create(expression=expression, result=result)
            message = "Ваше выражение добавлено."
        except ValueError:
            message = "Некорректный формат результата. Пожалуйста, укажите число."
    else:
        message = "Чтобы добавить выражение, используйте формат: /new/?expression=<ваше_выражение>&result=<результат>"
    return render(request, 'new.html', {'message': message})