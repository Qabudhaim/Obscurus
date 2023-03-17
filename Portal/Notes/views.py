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
        'Notes': notes,
        'Theme': 'green'
    }
    
    return render(request, 'index.html', context)

@permission_required('', login_url='/login/')
def add_note(request):

    if request.method == "POST":
        form = NoteForm(request.POST or None)
        
        references = request.POST['references']

        if len(references) == 0:
            references_exist = False
        else:
            references_exist = True 

        if form.is_valid():

            if references_exist:
                references = references.split(',')
                for link in references:
                    if validators.url(link):
                        continue
                    else:
                        messages.error(request, ("References are invalid!"))
                        return redirect('/notes/add_note/')
        
            note_instance = form.save()

            if references_exist:
                for link in references:
                    reference_instance = Reference(link=link, note=note_instance)
                    reference_instance.save()
            
            return redirect('/notes/')
                    
        else:
            messages.error(request, ("Form is invalid! Fill the required fields."))
            return redirect('/notes/add_note/')

    return render(request, 'add_note.html', {})