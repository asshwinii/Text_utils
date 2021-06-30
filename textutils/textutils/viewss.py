# I have created this file - Ashwini

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    charcounter = request.GET.get('charcounter','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params ={'purpose': 'removed punctions','analyzed_text':
                 analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext :
            analyzed = analyzed+ char.upper()
        params ={'purpose':'ALL CAPS', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremover == "on":
        analyzed =""
        for char in djtext :
            if char != "\n" :
                analyzed = analyzed + char
        params ={'purpose':'New line removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcounter== "on":

        count =0
        for char in djtext:
            count = count+1
        analzyed = "total char used are "+ str(count)
        params ={'purpose':'char counter','analyzed_text': analzyed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')

