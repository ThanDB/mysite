from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {})

# Create your views here.
def contact(request):
    return render(request, 'blog/contact.html', {})

# Create your views here.
def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

# Create your views here.
def profile(request):
    return render(request, 'blog/profile.html', {})

# Create your views here.
def resume(request):
    return render(request, 'blog/resume.html', {})