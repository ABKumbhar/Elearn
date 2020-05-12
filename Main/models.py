from django.db import models
# Create your models here.

def upload_path(instance,filename):
    if instance == Course:
        return '/'.join(['PDF',str(instance.id),filename])
    else:
        return '/'.join(['PDF',str(instance.course),filename]) 

class Student(models.Model):
    name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    title = models.CharField(null=True,max_length=50)
    PreviewText = models.TextField(null=True)
    PreviewFile = models.FileField(null=True,blank=True,upload_to = upload_path)

    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length = 50)
    number = models.IntegerField(null=True)
    File = models.FileField(null=True,blank=True,upload_to =upload_path)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
