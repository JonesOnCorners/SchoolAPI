# Generated by Django 2.2.2 on 2019-07-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190721_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.TextField(choices=[('CSE', 'CSE'), ('SO', 'Electronics and Telecom')]),
        ),
    ]
