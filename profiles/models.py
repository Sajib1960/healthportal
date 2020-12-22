from django.db import models
from django.contrib.auth.models import User, auth, AbstractUser
import datetime
# Create your models here.


class Person(AbstractUser):
    is_normal = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='pics/')
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(default=datetime.date.today())
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=1000)


class Professional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.person.username


class Normal(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.person.username


class Message(models.Model):
    message_details = models.TextField(max_length=4000)
    sent_from = models.ForeignKey(Person, related_name='sent_from', on_delete=models.CASCADE,)
    sent_to = models.ForeignKey(Person, related_name='sent_to', on_delete=models.CASCADE,)
    sent_at = models.DateTimeField(auto_now_add=True)
    mark_as_read = models.BooleanField(default=False)