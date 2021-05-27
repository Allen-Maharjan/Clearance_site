from .models import *


def Student_form(username, email):
    new_entry = Student.objects.create(
        name=username, phone=None, email=email)


def createTable(id, username):
    Department_choices = ['Computer Lab', 'Physics Lab', 'Account',
                          'Bus', 'Library', 'School/Dept Administration', 'Student Welfare']

    for i in Department_choices:
        new_entry = Clearance.objects.create(Department=i, Clear=None,
                                             DateCleared=None, student=id, name=username)
        new_entry.save()
