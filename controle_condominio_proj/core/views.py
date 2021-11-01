from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def soma(request,n1,n2):
    return HttpResponse('Soma: {}'.format(n1+n2))

def mult(request,n1,n2):
    return HttpResponse('Multiplicação: {}'.format(n1*n2))

def div(request,n1,n2):
    return HttpResponse('Divisão: {}'.format(n1/n2))

def sub(request,n1,n2):
    return HttpResponse('Subtração: {}'.format(n1-n2))

def page(request):
    return render()
