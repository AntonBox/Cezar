from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from apps.core.forms import CheckDataForm


def cezar(request):
    return render(request, 'index.html')


def code(request):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    data = json.loads(request.body.decode("utf-8"))
    form = CheckDataForm(data)
    if form.is_valid():
        N = form.cleaned_data['rotate']
        text = form.cleaned_data['code']
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
    else:
        return HttpResponse(status=400)


def uncode(request):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    data = json.loads(request.body.decode("utf-8"))
    form = CheckDataForm(data)
    if form.is_valid():
        N = form.cleaned_data['rotate']
        text = form.cleaned_data['code']
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
    else:
        return HttpResponse(status=400)


def scan(request):
    '''Суть заключается в том, что в английском почти в каждом предложении
    используется союз 'a': 'this is a pensil, this is a pen'.
    это очень часто используемое слово из одной буквы
    соответственно в зашифрованном тексте N=2  слово "а" будет словом 'c'
    вот если в тексте встречается слово из одной буквы, то скорее всего
    это буква "а" смещенная на N позиций, а значит шифр этого текста равен 'N'
    на живых текстах работает в большинстве случаев работает.
     '''
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    data = json.loads(request.body.decode("utf-8"))
    text = data['code'].lower()
    text = text.split(' ')
    N = 0
    for word in text:
        for letter in alpha:
            if word == letter:
                N = alpha.index(letter)
    if N == 0:
        read = 'Совпадений не найдено'
    else:
        read = 'Система обнаружила шифр с N =%d' % (N)
    return JsonResponse(read, safe=False)
