from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *

# Forum Home View - List all Categories
def forum(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    recent_posts = RecentPost.objects.all().order_by('-timestamp')[:5]  # Display recent 5 posts
    return render(request, 'forum.html', {
        'categories': categories,
        'posts': posts,
        'recent_posts': recent_posts,
    })

# View Posts in a Category
def category_posts(request, id):
    category = get_object_or_404(Category, id=id)  # Get the category by ID or 404 if not found
    posts = Post.objects.filter(category=category)  # Filter posts by the selected category
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

# View a Single Post and its Comments
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('-created_at')

    # Handle the comment submission form
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('forum:post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

# Create a New Post (only for authenticated users)
@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, pk=category_id)
        
        # Create the post
        post = Post.objects.create(title=title, content=content, user=request.user, category=category)
        
        return redirect('forum:category_posts', category_id=category.id)
    categories = Category.objects.all()
    return render(request, 'create_post.html', {'categories': categories})
