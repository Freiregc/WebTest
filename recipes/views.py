from django.shortcuts import render

def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'xD'})

def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', context={'name': 'xD'})
# Create your views here.
