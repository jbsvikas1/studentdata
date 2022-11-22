from django.db import models

# Create your models here.
class student(models.Model):
	sid=models.CharField(max_length=20)
	sname=models.CharField(max_length=100)
	semail=models.EmailField()
	scontact=models.CharField(max_length=15)
	def _str_(self):
		return "%s" %(self.sname)
	class Meta:
		db_table="studentdata"
