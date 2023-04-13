from django.shortcuts import render, HttpResponse, redirect

# Create your views here.



def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == "GET":
        return render(request, 'posts/posts.html')

