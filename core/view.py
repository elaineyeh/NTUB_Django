from django.http import HttpResponse
from django.shortcuts import render

def root(request, n1, n2):
    return HttpResponse(n1+n2)

def hi(request, n1, n2):
    s = n1+n2

    return render(request, 'hi.html', {
        's': s,
    })

def r(request, start, stop, n):
    step = 2

    if stop < start:
        start, stop = stop, start

    if n == 0:
        if start%2 == 1:
            start += 1

        rr = range(start, stop+1, step)
    elif n == 1:
        if start%2 == 0:
            start += 1

        rr = range(start, stop+1, step)
    else:
        rr = range(start, stop+1)

    return render(request, 'a.html', {
        'rr':rr,
    })

def tag_test(request):
    ll = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'tag_test.html', {
        'll':ll,
    })