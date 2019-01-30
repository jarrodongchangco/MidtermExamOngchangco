from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.



class Position(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)

class Candidate(models.Model):

	firstname = models.CharField(max_length=250)
	lastname = models.DateTimeField(default=timezone.now)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	birthdate = models.DateTimeField()
	platform = models.TextField(default=True)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Candidate"
		verbose_name_plural = "Candidates"

	def __str__(self):
		return str(self.firstname)

	def get_absolute_url(self):
		return reverse('candidate-detail', kwargs={'pk': self.pk})

class Vote(models.Model):
    name = models.CharField(max_length=250)
    #vote_datetime = models.ForeignKey(default=timezone.now)
