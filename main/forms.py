from django.forms import ModelForm, TextInput, Textarea
from .models import Note


class NoteForm(ModelForm):
	class Meta:
		model = Note
		fields = ['title', 'text']

		widgets = {
			'title':TextInput(attrs={
				'class':'add-form',
				'placeholder':'Note Title',
			}),
			'text':Textarea(attrs={
				'class':'add-form text-form',
				'placeholder':'Note Text',
			}),
		}