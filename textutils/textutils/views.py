# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

####
# def index(request):
#     return HttpResponse('''<a href = "https://www.facebook.com/">New to learn</a>''')
#     # return HttpResponse("Hello RoY")

# def about(request):
#     return HttpResponse("Hello about RoY")

# def name(request):
#     return HttpResponse("Name is Roy")

# def abname(request):
#     file = open("f1.txt",'r+')
#     return HttpResponse(file.read())
#     # return HttpResponse("Nilanjan RoY")

####
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctions', 'analyzed_text':analyzed}
        djtext = analyzed
    # Analyse the text
        # return render(request, 'analyze.html', params)
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UPPER', 'analyzed_text':analyzed}
        djtext = analyzed
    # Analyse the text
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text':analyzed}
        djtext = analyzed
    # Analyse the text
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text':analyzed}
    # Analyse the text
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        count = 0
        for i in djtext:
            count+=1
        params = {'purpose': 'Character Count', 'analyzed_text':count}
    # Analyse the text
        # return render(request, 'analyze.html', params)


    if removepunc!="on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Select any operation...")
    
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("cap first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove <a href = '/'>back</a>")

# def charcount(request):
#     return HttpResponse("char count")

