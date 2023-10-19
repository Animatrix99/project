from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import Post
from .form import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostViev(View):
    '''yangiliklar'''
    def get(self, request):
        '''Yangiliklar'''
        posts = Post.objects.order_by('-id')
        paginator = Paginator(posts, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'home.html', {"page_obj" : page_obj})
    

class PostDetail(View):
    '''Batafsil malumot'''
    def get(self, request, pk):
        '''Yangiliklar'''
        post = Post.objects.get(id=pk)
        return render(request, 'post_detail.html', {"post": post})
    

class PostCreate(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'tixt', 'author', 'date', 'img']


class BlogUpdte(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'tixt', 'img']

class BlogDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


