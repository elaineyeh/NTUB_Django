from django.http import HttpResponse
from django.shortcuts import render

def root(request, n1, n2):
    return HttpResponse(n1+n2)

def hi(request, n1, n2):
    s=n1+n2
    return render(request, 'hi.html', {
        's':s,
    })

def r(request, start, stop):
    if stop < start:
        start, stop=stop, start
    rr=range(start, stop+1)
    return render(request, 'a.html', {
        'rr':rr,
    })