from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'vishal','place':'jupiter'}
    return render(request, 'index.html', params)
def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>

               <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 

               <a href="https://www.facebook.com/vishal.sagar.946">Facebook</a><br>

               <a href="https://www.flipkart.com/">Flipkart</a><br>

               <a href="https://www.hindustantimes.com">News</a><br>

               <a href="https://www.google.com/">Google</a>'''

    return HttpResponse(s)

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcaps','default')
    smallcaps=request.POST.get('smallcaps','default')
    removenewline=request.POST.get('removenewline','default')
    spaceremover=request.POST.get('spaceremover','default')
    charcount=request.POST.get('charcount','default')
    # print(removepunc)
    # print(djtext)
    if (removepunc =="on"):
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (smallcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Change to lowercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (removenewline == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Change to removenewline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Change to spaceremover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charcount == "on"):
        print(djtext)
        analyzed = len(djtext)

        params = {'purpose': 'Change to charcount', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc!="on" and fullcaps!="on" and smallcaps!= "on" and removenewline!= "on" and spaceremover!= "on" and charcount!= "on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)
# def capitalizefirst(request):
#     return HttpResponse("<h1>capitalizefirst</h1>")
# def newlineremove(request):
#     return HttpResponse("<h1>newlineremove</h1>")
# def spaceremove(request):
#     return HttpResponse("<h1>spaceremove<a href='/'>back</a></h1>")
# def charcount(request):
#     return HttpResponse("<h1>charcount</h1>")
#
