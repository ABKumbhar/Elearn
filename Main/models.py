from django.db import models
# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['Files_courses',filename])

class Student(models.Model):
    name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='profilepic/')
    Linkdein = models.URLField(max_length=500,null=True,blank=True)
    Phone = models.CharField(max_length=12, null=True)
    skype_ID = models.CharField(max_length=500, null=True)



    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='profilepic/')
    Linkdein = models.URLField(max_length=500,null=True)
    Institute_Organization = models.CharField(max_length=200,null=True)
    Education = models.CharField(max_length=200,null=True)
    Specialization = models.CharField(max_length=200,null=True)
    Quote = models.TextField(null=True, blank=True)
    skype_ID = models.CharField(max_length=500, null=True)



    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey('Teacher',related_name='courses',on_delete=models.CASCADE)
    title = models.CharField(null=True,max_length=50,unique=True)
    PreviewText = models.TextField(null=True)
    PreviewFile = models.FileField(null=True,blank=True,upload_to = upload_path)
    ratings = models.FloatField(null=True)
    assignment = models.FileField(null=True, blank=True,upload_to = upload_path)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey('Course',related_name='modules',on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length = 50,unique=True)
    number = models.IntegerField(null=True)
    File = models.FileField(null=True,blank=True,upload_to =upload_path)
    content = models.TextField(null=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title
