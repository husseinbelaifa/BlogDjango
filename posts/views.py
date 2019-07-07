from django.shortcuts import render
from django.http import HttpResponse
from django_seed import Seed
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.
from .models import Posts
def index(request):

   

    postsList=Posts.objects.all()

    paginator=Paginator(postsList,10)

    page=request.GET.get('page')

    posts=paginator.get_page(page)

    context={
         'title':'Posts',
         'posts':posts
    }

  

    return render(request,'posts/index.html',context)

def show(request,id):
    post=Posts.objects.get(id=id)

    context={
        
        'post':post
    }

    return render(request,'posts/show.html',context)

def init(request):

    seeder=Seed.seeder()
    seeder.add_entity(User,20)
    seeder.add_entity(Posts,100)
    inserted_pks = seeder.execute()

    return HttpResponse('data was inisialized')



