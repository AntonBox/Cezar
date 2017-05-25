from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json


def cezar(request):
    return render(request, 'index.html')


def code(request):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    data = json.loads(request.body.decode("utf-8"))
    text = data['code'].lower()
    try:
        N = int(data['rotate'])
    except ValueError:
        return HttpResponse(status=400)
    if N not in range(0, len(alpha) + 1):
        return HttpResponse(status=400)
    coded_text = []
    for letter in text:
        if letter in alpha:
            number = alpha.index(letter) + N
            if number > len(alpha) - 1:
                number = len(alpha) - alpha.index(letter)
                number = N - number
            letter = alpha[number]
        coded_text.append(letter)
    read = ''.join(coded_text)
    return JsonResponse(read, safe=False)


def uncode(request):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    data = json.loads(request.body.decode("utf-8"))
    text = data['code'].lower()
    try:
        N = int(data['rotate'])
    except ValueError:
        return HttpResponse(status=400)
    if N not in range(0, len(alpha) + 1):
        return HttpResponse(status=400)
    uncoded_text = []
    for letter in text:
        if letter in alpha:
            number = alpha.index(letter) - N
            if number < 0:
                number = len(alpha) - N + alpha.index(letter)
            letter = alpha[number]
        uncoded_text.append(letter)
    read = ''.join(uncoded_text)
    return JsonResponse(read, safe=False)
