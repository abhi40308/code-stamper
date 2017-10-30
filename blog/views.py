from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def home(request):
	posts = Post.objects.filter(section__iexact='home').order_by('-published_date')
	return render(request, 'blog/home.html', {'posts' : posts})

def news(request):
	posts = Post.objects.filter(section__iexact='news').order_by('-published_date')
	return render(request, 'blog/news.html', {'posts' : posts})

def internet(request):
	posts = Post.objects.filter(section__iexact='internet').order_by('-published_date')
	return render(request, 'blog/internet.html', {'posts' : posts})

def apps_games(request):
	posts = Post.objects.filter(section__iexact='apps_games').order_by('-published_date')
	return render(request, 'blog/apps_games.html', {'posts' : posts})

def entrepreneur(request):
	posts = Post.objects.filter(section__iexact='entrepreneur').order_by('-published_date')
	return render(request, 'blog/entrepreneur.html', {'posts' : posts})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
