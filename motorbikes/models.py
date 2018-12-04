from django.db import models
from django.utils import timezone

class Brand_MB(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self): 
		return self.name


class Model_MB(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self): 
		return self.name



class Post_MB(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand_MB, on_delete=models.CASCADE)
    model = models.ForeignKey(Model_MB, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.FileField()
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
