from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	banner_image = models.ImageField(upload_to="category/banners")

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	price = models.FloatField()
	details = models.TextField()
	quantity = models.IntegerField()
	in_stock = models.BooleanField(default=True)
	date_add = models.DateField(default=timezone.now)

	def __str__(self):
		return self.title
