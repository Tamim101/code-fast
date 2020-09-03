from django.shortcuts import render, get_object_or_404
from .models import blog

def all_blog(request):

    blogs = blog.objects.all()

    return render (request, 'blog/all_blogs.html', {'blog':blogs})



def detail(request, blog_id):


    blogs = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blogs})
