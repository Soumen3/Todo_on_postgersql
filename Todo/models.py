from django.db import models

# Create your models here.
class Todo(models.Model):

	task = models.TextField()
	completed = models.BooleanField(default=False, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title