from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog_page.html')

def blogDetail(request):
    return render(request, 'blog_details.html')

