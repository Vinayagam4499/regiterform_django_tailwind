from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    address = models.TextField()

    def __str__(self):
        return self.name
