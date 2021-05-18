from django.shortcuts import render, HttpResponse

import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

# Create your views here.
def Home(request):
    #return HttpResponse("this is homepage")
    return render(request,'Home.html')

def About_Covid(request):
    #return HttpResponse("this is about page")
    return render(request,'About_Covid.html')

def Contact(request):
    #return HttpResponse("this is contact page")
    return render(request,'Contact.html')

def Test_Yourself(request):
    #return HttpResponse("take a covid selftest")
    return render(request,'Test_Yourself.html')

def Covid_Forecast(request):
    #return HttpResponse("this is about page")
    return render(request,'Covid_Forecast.html')

def Global_Trend(request):
    #return HttpResponse("this is about page")
    return render(request,'Global_Trend.html')

def India_Trend(request):
    #return HttpResponse("this is about page")
    return render(request,'India_Trend.html')


def bot_search(request):
    query= request.GET.get('query')

    try:
        client=wolframalpha.client("")
        res=client.query(query)
        ans= next(res.results).text
        return render(request,'Test_Yourself.html',{'ans':ans,'query':query})

    except Exception:
        try:
            ans= wikipedia.summary(query,sentences=10)
            return render(request,'Test_Yourself.html',{'ans':ans,'query':query})
    
    
        except Exception:
             ans="FOUND NOTHING"
             return render(request,'Test_Yourself.html',{'ans':ans,'query':query})

