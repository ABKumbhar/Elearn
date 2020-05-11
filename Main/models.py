from django.db import models
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    title = models.CharField(null=True,max_length=50)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    titlem = models.CharField(null=True, max_length = 20)
    index_number = models.IntegerField(unique=True, null=True) 
    content = models.TextField(null=True)

    def __str__(self):
        return self.titlem
