from django.shortcuts import render
from .services import post_services
# Create your views here.

def listar_post(request):
    posts = post_services.listar_post()
    return render( request, 'posts.html', {'posts': posts})


def listar_post_id(request, id):
    post = post_services.listar_post_id(id)
    return render(request, 'post.html', {'post': post})