# I have created this file- Tanmoy
from django.http import HttpResponse
from django.shortcuts import render
import string
from language_tool_python import LanguageTool
def index(request):
    params={'name':'Tanmoy','place':'Pune'}
    return render(request,'index.html',params)
def Style2(request):
    return render(request,'Style2.html')
def About(request):
    return render(request,'about.html')
def Home(request):
    return render(request, 'index.html')
def analyze(request):
    orgtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    removespace=request.POST.get('removespace','off')
    uppercase=request.POST.get('Uppercase','off')
    grammer=request.POST.get('GrammarCheck','off')
    wordcount=request.POST.get('Wordcount','off')
    charcount=request.POST.get('CharCount','off')
    capfirst=request.POST.get('CapFirst','off')
    if(removepunc=='on' and removespace=='off'):
        translator=str.maketrans('', '', string.punctuation)
        res=orgtext.translate(translator)
        params={'purpose': 'Removed Punctuations','analyzed_text':res,'Userinp':removepunc}
        return render(request,'analyze.html',params)
    elif(removespace=='on' and removepunc=='off'):
        words = orgtext.split()
        cleaned_text = ' '.join(words)
        params={'purpose':'Removed Extra Spaces','analyzed_text':cleaned_text,'Userinp':removespace}
        return render(request, 'analyze.html', params)
    elif(removespace=='on' and removepunc=='on'):
        words = orgtext.split()
        cleaned_text = ' '.join(words)
        translator = str.maketrans('', '', string.punctuation)
        res = cleaned_text.translate(translator)
        params = {'purpose': 'Removed Extra Spaces & Removed Punctuations', 'analyzed_text': res}
        return render(request, 'analyze.html', params)
    elif(uppercase=='on'):
        res=orgtext.upper()
        params={'purpose':'Uppercase','analyzed_text':res,'Userinp':uppercase}
        return render(request,'analyze.html',params)
    elif(wordcount=='on'):
        text=list(orgtext.split())
        res=len(text)
        params = {'purpose': 'Word Counter', 'analyzed_text': res,'Userinp':wordcount}
        return render(request,'analyze.html',params)
    elif(charcount=='on'):
        res=len(orgtext.replace(" ", ""))
        params = {'purpose': 'Char Counter', 'analyzed_text': res,'Userinp':charcount}
        return render(request,'analyze.html',params)
    elif(grammer=='on'):
        tool = LanguageTool('en-US')
        corrected = tool.correct(orgtext)
        params={'purpose':'Corrected Grammaer','analyzed_text':corrected,'Userinp':grammer}
        return render(request,'analyze.html',params)
    elif(capfirst=='on'):
        res=orgtext.title()
        params = {'purpose': 'Capitalize First Letter', 'analyzed_text': res,'Userinp':capfirst}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error in selection")

