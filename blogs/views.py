from django.shortcuts import render, get_object_or_404
from .models import Blog, Category


def home(request):
    blogs = Blog.objects.filter(status='published').order_by('-created_at')[:6]
    categories = Category.objects.all()

    return render(request, 'blogs/home.html', {
        'blogs': blogs,
        'categories': categories
    })


def blog_list(request):
    blogs = Blog.objects.filter(status='published').order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'blogs/blog_list.html', {
        'blogs': blogs,
        'categories': categories
    })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='published')

    return render(request, 'blogs/blog_detail.html', {
        'blog': blog
    })


def category_blogs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category, status='published').order_by('-created_at')

    return render(request, 'blogs/category_blogs.html', {
        'category': category,
        'blogs': blogs
    })


def search_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(status='published')

    if query:
        blogs = blogs.filter(title__icontains=query)

    return render(request, 'blogs/search.html', {
        'blogs': blogs,
        'query': query
    })