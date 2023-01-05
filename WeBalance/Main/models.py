from django.db import models
from django.contrib.auth.models import User

class Preferences(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	emails = models.IntegerField()
	calls = models.IntegerField()
	hours = models.IntegerField()
	meetings = models.IntegerField()
	breaks = models.IntegerField()

class WorkDone(models.Model):
	class Meta:
		ordering = ['date']

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	emails = models.IntegerField()
	calls = models.IntegerField()
	hours = models.IntegerField()
	meetings = models.IntegerField()
	breaks = models.IntegerField()

class Flagged(models.Model):
	class Meta:
		ordering = ['date_flagged']

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_flagged = models.DateField()
	flag = models.CharField(max_length=50)
	preference = models.IntegerField()
	work_done = models.IntegerField()
	action_taken = models.BooleanField(default=False)

