# Generated by Django 2.2.2 on 2019-07-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190721_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_credits',
            field=models.IntegerField(default='10'),
        ),
    ]
