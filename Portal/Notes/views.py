from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from Notes.forms import NoteForm
from Notes.models import Note, Reference
from django.contrib import messages
from taggit.models import Tag


@permission_required('', login_url='Core:login')
def index(request):
    notes = Note.objects.all().order_by('-id')

    context = {
        'Notes': notes,
        'Theme': 'green'
    }
    
    return render(request, 'index.html', context)

@permission_required('', login_url='Core:login')
def add_note(request):

    tags = Tag.objects.all()

    if request.method == "POST":
        list_of_tags = request.POST.getlist('tags')
        print("*****")
        print(list_of_tags)
        print("*****")

        form = NoteForm(request.POST or None, request=request)

        if form.is_valid():
            references = form.cleaned_data.pop('references')

            print(form.cleaned_data)

            note_instance = form.save()

            for url in references:
                reference_instance = Reference(url=url, note=note_instance)
                reference_instance.save()

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