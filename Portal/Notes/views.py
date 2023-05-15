from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from Notes.forms import NoteForm
from Notes.models import Note, Reference
from django.contrib import messages
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from Notes.operations import save_image_from_url
from django.http import HttpResponse
import shutil
from django.conf import settings

@permission_required('', login_url='Core:login')
def index(request):

    query = request.GET.get('query', '')

    notes_list = Note.objects.filter(Q(tags__name__icontains=query) | Q(title__icontains=query)).order_by('-id').distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(notes_list, 8)

    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    context = {
        'Notes': notes,
    }
    
    return render(request, 'index.html', context)

@permission_required('', login_url='Core:login')
def add_note(request):

    tags = Tag.objects.all().order_by('-id')

    if request.method == "POST":

        form = NoteForm(request.POST or None, request=request)

        if form.is_valid():
            references = form.cleaned_data.pop('references')

            note_instance = form.save()

            for url in references:
                reference_instance = Reference(url=url, note=note_instance)
                reference_instance.save()

            if note_instance.cover:
                save_image_from_url(note_instance.cover, f'{settings.MEDIA_ROOT}/{note_instance.id}/cover.jpg')

            return redirect('Notes:index')
                    
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

            return redirect('Notes:add_note')
    
    context = {
        'Tags': tags
    }
    return render(request, 'add_note.html', context)

@permission_required('', login_url='Core:login')
def show_note(request, id):

    note = Note.objects.get(id=id)
    
    context = {
        'Note': note,
    }
    return render(request, 'show_note.html', context)

@permission_required('', login_url='Core:login')
def delete_note(request, id):

    note = Note.objects.get(id=id)
    note.delete()

    if note.cover:
        shutil.rmtree(f'{settings.MEDIA_ROOT}/{id}')
    
    return redirect('Notes:index')

@permission_required('', login_url='Core:login')
def update_note(request, id):

    note = get_object_or_404(Note, id=id)
    tags = Tag.objects.all().order_by('-id')
    
    if request.method == "POST":

        form = NoteForm(request.POST or None, instance=note, request=request)

        if form.is_valid():

            references = form.cleaned_data.pop('references')
            note_references = note.references.all()
            note_references.delete()

            note_instance = form.save()
            
            for url in references:
                reference_instance = Reference(url=url, note=note_instance)
                reference_instance.save()

            if note_instance.cover:
                save_image_from_url(note_instance.cover, f'/home/admin/Obscurus/Portal/media/{note_instance.id}/cover.jpg')
                
            return redirect('Notes:show_note', id)
                    
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

            return redirect('Notes:add_note')
        
    context = {
        'Note': note,
        'Tags': tags
    }
    return render(request, 'update_note.html', context)


@permission_required('', login_url='Core:login')
def export_note(request, id):

    note = Note.objects.get(id=id)
    
    response = HttpResponse(note.body, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={note.title}.md'

    return response
