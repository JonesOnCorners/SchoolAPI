# Generated by Django 2.2.2 on 2019-07-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField()),
                ('course_semester', models.DateField()),
                ('course_credits', models.IntegerField()),
            ],
        ),
    ]
