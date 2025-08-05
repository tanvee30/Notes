from django.shortcuts import render, redirect
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from .models import Note
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard')  # Or you can show a list of notes later
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})
    




@login_required
def view_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/view_notes.html', {'notes': notes})



@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('view_notes')
    
    return render(request, 'notes/edit_note.html', {'note': note})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('view_notes')

