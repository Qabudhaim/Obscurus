from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from Notes.forms import NoteForm
from Notes.models import Note, Reference
from django.contrib import messages
import validators

@permission_required('', login_url='/login/')
def index(request):
    notes = Note.objects.all().order_by('-id')

    context = {
        'Notes': notes
    }
    
    return render(request, 'index.html', context)

@permission_required('', login_url='/login/')
def add_note(request):

    if request.method == "POST":
        form = NoteForm(request.POST or None)
        references = request.POST['references']
       
        if form.is_valid():
            print(type(references))
            references = references.split(',') or None
            print(references)
            print(type(references))
            for link in references:
                if validators.url(link):
                    continue
                else:
                    messages.error(request, ("References are invalid!"))
                    return redirect('/notes/add_note/')
        
            note_instance = form.save()

            for link in references:
                reference_instance = Reference(link=link, note=note_instance)
                reference_instance.save()
        else:
            print(form.is_valid())

        return redirect('/notes/')


    return render(request, 'add_note.html', {})