from django.db import models

# Create your models here.

class Haat(models.Model):
	name = models.CharField(max_length = 50)
	address = models.TextField()
	info = models.TextField()
	theme = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Stall(models.Model):
	haat = models.ForeignKey(Haat, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50)
	stallNumber = models.IntegerField()
	story = models.TextField()
	tags = models.TextField(null=True, blank=True)
	imageURL = models.CharField(max_length = 500)
	
	def __str__(self):
		return self.name

class Rating(models.Model):
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	userName = models.CharField(max_length = 50)
	value = models.IntegerField()
	issueDate = models.DateTimeField(auto_now_add=True)
	text = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.userName + "---" + str(self.stall.name) + "---" + self.stall.haat.name


class Product(models.Model):
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50)
	description = models.TextField()
	price = models.IntegerField()
	promotions = models.TextField(null=True, blank=True)
	imageURL = models.CharField(max_length = 500)

	def __str__(self):
		return self.name + "---" + str(self.stall.name) + "---" + self.stall.haat.name