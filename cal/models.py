from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
	day=models.DateField(default=date.today())
	start_time=models.TimeField()
	end_time=models.TimeField()
	notes=models.CharField(max_length=200)
	name=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.notes

	class Meta:
		verbose_name_plural='Events'

	def get_html_url(self):
		url=reverse('cal:event_edit',args=[self.id])
		return '<a href="%s">%s</a>'%(url,str(self.notes))
