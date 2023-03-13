from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def handler404(request, *args, **argv):
    context = {
        'Name': 'Error404',
        'Message': 'Page Not Found'
    }
    return render(request, 'error_template.html', context, status=404)

def handler500(request, *args, **argv):
    context = {
        'Name': 'Error500',
        'Message': 'Internal Server Error'
    }
    return render(request, 'error_template.html', status=500)

def handler403(request, *args, **argv):
    context = {
        'Name': 'Error403',
        'Message': 'Permission Denied'
    }
    return render(request, 'error_template.html', status=403)

def handler400(request, *args, **argv):
    context = {
        'Name': 'Error400',
        'Message': 'Bad Request'
    }
    return render(request, 'error_template.html', status=400)
