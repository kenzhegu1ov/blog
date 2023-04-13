from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def first_view(request):
    if request.method == 'GET':
        return HttpResponse('Its first view')

def redirect_to_youtube(request):
    if request.method == 'GET':
        return redirect("https://youtube.com/")

def redirect_to_google(request):
    if request.method == 'GET':
        return redirect("https://google.com/")