from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    userText = request.GET['userText']
    wordslist = userText.split()
    wordsdict = {}

    for word in wordslist:
        if word in wordsdict:
            wordsdict[word] += 1
        else:
            wordsdict[word] = 1
    sortedWords = sorted(
        wordsdict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'userText': userText, 'count': len(wordslist), 'sortedWords': sortedWords})
