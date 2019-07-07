from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Posts
def index(request):
    # return HttpResponse('Hello From Post Router')

    posts=Posts.objects.all()[:10]

    context={
         'title':'Latest Posts',
         'posts':posts
    }
    return render(request,'posts/index.html',context)
