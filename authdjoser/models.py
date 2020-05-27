from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    Teacher = 'T'
    Student = 'S'
    Typeofuser = [
    (Teacher , 'Teacher'),
    (Student, 'Student'),
    ]
    Type_of_user = models.CharField(
        max_length=1,
        choices=Typeofuser,
        default=Student,
    )


    REQUIRED_FIELDS = ['username', 'first_name','last_name', 'Type_of_user']
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email

# Create your models here.
