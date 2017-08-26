from django.db import models
from details.models import Product, Stall

# Create your models here.

class Sale(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now=True)
	salePrice = models.IntegerField()

	def __str__(self):
		return str(self.id)

class Inventory(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	total = models.IntegerField()

	def __str__(self):
		return self.product.name + "_inventory"

class ProductHit(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.product.name + "_hits"

class StallHit(models.Model):
	stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.stall.name + "_hits"