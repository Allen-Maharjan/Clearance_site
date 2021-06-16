from django.db import models
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User


class Updateinfo(models.Model):

    Status = (
        ('All Clear', 'All Clear'),
        ('Semi Clear', 'Semi Clear'),
        ('Not cleared', 'Not Cleared')
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
    DateCleared = models.DateTimeField(null=True)
    name = models.CharField(max_length=200, null=True)
    ClearedBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    AmountLeft = models.IntegerField(null=True)

    class Meta:
        unique_together = (("student", "Department", "name", "Clear"),)
