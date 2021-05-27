from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Clearance(models.Model):

    Status = (
        ('All Clear', 'All Clear'),
        ('Semi Clear', 'Semi Clear')
    )

    Department_choices = (
        ('Computer Lab', 'Computer Lab'),
        ('Physics Lab', 'Physics Lab'),
        ('Account', 'Account'),
        ('Bus', 'Bus'),
        ('Library', 'Library'),
        ('School/Dept Administration', 'School/Dept Administration'),
        ('Student Welfare', 'Student Welfare')
    )
    student = models.IntegerField(null=True)
    Department = models.CharField(
        max_length=200, null=True, choices=Department_choices)
    Clear = models.CharField(max_length=200, null=True, choices=Status)
    DateCleared = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (("student", "Department", "name"),)
