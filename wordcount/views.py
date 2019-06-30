
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def page_one(request):
    return render(request, 'page_1.html', {'text':'Hello from backebd'})


def count(request):
    text = request.GET['text']
    worddictionaty = {}
    wordlist = text.split()
    for word in wordlist:
        if word in worddictionaty:
            # increment
            worddictionaty[word] += 1
        else:
            # add to the dictionary
            worddictionaty[word] = 1

    sortedwords = sorted(worddictionaty.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text':text, 'count':len(wordlist), 'worddictionaty':sortedwords})

def about(request):
    return render(request, 'about.html')
