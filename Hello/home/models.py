from django.db import models

# Create your models here.
# equivalent to SQL table
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField( max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
