from django.db import models


class updateInfo(models.Model):

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
    DateCleared = models.DateTimeField(null=True)
    name = models.CharField(max_length=200, null=True)
    ClearedBy = models.CharField(max_length=200, null=True)
    Email = models.EmailField(null=True)

    class Meta:
        unique_together = (("student", "Department", "name"),)
