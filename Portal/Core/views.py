from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

@permission_required('', login_url='Core:login')
def index(request):
    return render(request, 'base.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def login_user(request):
    if request.user.is_authenticated:
            return redirect('index')

    if request.method == "POST":
        next_page = request.GET.get('next', 'index')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_page)
        else:
            messages.error(request, ("Login failed! Try again."))
            return redirect(f'Core:login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('Core:login')

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
    return render(request, 'error_template.html', context, status=500)

def handler403(request, *args, **argv):
    context = {
        'Name': 'Error403',
        'Message': 'Permission Denied'
    }
    return render(request, 'error_template.html', context, status=403)

def handler400(request, *args, **argv):
    context = {
        'Name': 'Error400',
        'Message': 'Bad Request'
    }
    return render(request, 'error_template.html', context, status=400)
