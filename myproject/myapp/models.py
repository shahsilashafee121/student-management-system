from django.db import models


from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=20)
    class Meta:
        db_table='usertable'
        
class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    email=models.EmailField()
    gender=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    cnpassword=models.CharField(max_length=30)

class Notapproval(models.Model):
    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phoneno=models.IntegerField()
    age=models.IntegerField()
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    cnpassword=models.CharField(max_length=20)

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    email=models.EmailField()
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    phoneno=models.IntegerField()
    cnpassword=models.CharField(max_length=30)

class LeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)  
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)

