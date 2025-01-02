from django.shortcuts import render

   def index_page(request):
       context = {
           'author': 'Иван',
           'page_count': 3,
       }
       return render(request, 'index.html', context)
