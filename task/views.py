from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse({'slackUsername':'Jesse-Paul Osemeke', 'backend':True, 'age':18, 'bio':'I like to code!'})