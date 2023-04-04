from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} com {idade} anos</h1>')


def soma(request, num1, num2):
    sum = num1 + num2
    return HttpResponse(f"<h1>{num1} + {num2} = {soma}</h1>")


def multiplicacao(request, num1, num2):
    multiply = num1 * num2
    return HttpResponse(f"<h1>{num1} + {num2} = {multiply}</h1>")


def divisao(request, num1, num2):
    division = num1 / num2
    return HttpResponse(f"<h1>{num1} + {num2} = {division}</h1>")


def subtracao(request, num1, num2):
    subtract = num1 - num2
    return HttpResponse(f"<h1>{num1} + {num2} = {subtract}</h1>")
