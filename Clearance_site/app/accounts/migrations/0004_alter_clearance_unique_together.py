# Generated by Django 3.2.3 on 2021-05-25 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_clearance_department'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clearance',
            unique_together={('student', 'Department')},
        ),
    ]
