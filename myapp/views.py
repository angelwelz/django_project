from django.shortcuts import render
from datetime import datetime

def index_page(request):
   context = {
       'author': 'Иван',
       'page_count': 3,
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