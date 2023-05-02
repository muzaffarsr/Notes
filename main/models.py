from django.db import models


class Note(models.Model):
	title = models.TextField(blank = True, default = 'Title')
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add = True)