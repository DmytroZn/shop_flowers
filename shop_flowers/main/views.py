from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def main(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)

def main2(request):

    return JsonResponse({'foo':'bar'})
