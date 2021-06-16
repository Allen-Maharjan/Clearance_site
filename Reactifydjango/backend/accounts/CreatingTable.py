from .models import *


def Student_form(username, email):
    new_entry = Student.objects.create(
        name=username, phone=None, email=email)

    new_entry.save()


def createTable(id, username, email, user):
    Department_choices = ['Computer Lab', 'Physics Lab', 'Account',
                          'Bus', 'Library', 'School/Dept Administration', 'Student Welfare']

    for i in Department_choices:
        new_entry = Clearance.objects.create(Department=i, Clear=None,
                                             DateCleared=None, student=id, name=username, ClearedBy=user, Email=email, AmountLeft=None)
        new_entry.save()
