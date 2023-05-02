from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def home(request):
	notes = Note.objects.order_by('-pub_date')

	context = {
		'notes':notes,
	}
	return render(request, 'main/index.html', context)

def add_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		form.save()
		return redirect('home')

	form = NoteForm()

	context = {
		'form':form,
	}
	return render(request, 'main/add_note.html', context)

def note(request, nid):
	note = Note.objects.get( id = nid )

	context = {
		'note':note,
	}
	return render(request, 'main/note.html', context)

def remove(request, nid):
	if request.method == 'POST':
		note = Note.objects.get( id = nid )
		note.delete()
		return redirect('home')

def edit(request, nid):
	note = Note.objects.get( id = nid )
	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		form.save()
		return redirect('home')
	form = NoteForm(instance=note)

	context = {
		'form':form,
	}
	return render(request, 'main/edit_note.html', context)