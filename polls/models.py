import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
	"""docstring for Question"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pud_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
						