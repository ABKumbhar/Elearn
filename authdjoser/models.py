from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    TEACHER = 'T'
    STUDENT = 'S'
    usertype = [
    (TEACHER , 'TEACHER'),
    (STUDENT , 'STUDENT'),
    ]
    Typeofuser = models.CharField(
        max_length=1,
        choices=usertype,
        default=STUDENT,
    )
    #flag = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username', 'first_name','last_name', 'Typeofuser']
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email

# Create your models here.
