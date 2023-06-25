from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from taggit.models import Tag

@permission_required('', login_url='Core:login')
def index(request):
    return render(request, 'base.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def login_user(request):
    if request.user.is_authenticated:
            return redirect('Core:index')

    if request.method == "POST":
        next_page = request.GET.get('next', 'Notes:index')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_page)
        else:
            messages.error(request, ("Login failed! Try again."))
            return redirect('Core:login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('Core:login')


def user_settings(request):
    tags = Tag.objects.all().order_by('-id')

    context = {
        'Tags': tags
    }
    return render(request, 'user_settings.html', context)

def add_tag(request):
    tags_list = request.POST.get('tags').replace(" ", "").lower()
    tags_list = tags_list.split(',')

    tags = Tag.objects.all()

    for tag in tags_list:
        Tag.objects.get_or_create(name=tag)

    return redirect('Core:user_settings')


def remove_tag(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect('Core:user_settings')



def handler500(request, *args, **argv):
    context = {
        'Name': 'Error500',
        'Message': 'Internal Server Error'
    }
    return render(request, 'error_template.html', context, status=500)

def handler404(request, *args, **argv):
    context = {
        'Name': 'Error404',
        'Message': 'Page Not Found'
    }
    return render(request, 'error_template.html', context, status=404)

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
