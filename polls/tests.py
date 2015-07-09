from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.

class QuestionMethodTest(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		test = timezone.now()
		test2 = datetime.timedelta(days=1)
		print ('timezone.now():', test)
		print ('datetime.timedelta(days=1):', test2)
		print ('time:', time)
		# self.assertEqual(future_question.was_published_recently(), False)