from django.shortcuts import render
from django.http import HttpResponse
from django_seed import Seed
# Create your views here.
from .models import Posts
def index(request):

    posts=Posts.objects.all()[:10]

    context={
         'title':'Latest Posts',
         'posts':posts
    }

    # seeder=Seed.seeder()
    # seeder.add_entity(Posts,100)
    # inserted_pks = seeder.execute()

    #seed data posts


    return render(request,'posts/index.html',context)

def show(request,id):
    post=Posts.objects.get(id=id)

    context={
        
        'post':post
    }

    return render(request,'posts/show.html',context)

def init(request):

    seeder=Seed.seeder()
    seeder.add_entity(Posts,100)
    inserted_pks = seeder.execute()

    return HttpResponse('data was inisialized')



