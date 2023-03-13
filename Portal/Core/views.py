from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def handler404(request, *args, **argv):
    return render(request, 'errors/404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, 'errors/500.html', status=500)

def handler403(request, *args, **argv):
    return render(request, 'errors/403.html', status=403)

def handler400(request, *args, **argv):
    return render(request, 'errors/400.html', status=400)
