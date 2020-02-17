from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
    age = models.IntegerField()
    start_date = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.position + " " + str(self.salary)
