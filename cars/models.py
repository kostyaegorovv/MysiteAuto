from django.db import models
from django.utils import timezone

class Brand(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self): 
		return self.name


class Model(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self): 
		return self.name

def image_folder(instance, filename):
	filename = filename
	return filename


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title