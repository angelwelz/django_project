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
