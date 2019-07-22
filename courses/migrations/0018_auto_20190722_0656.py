# Generated by Django 2.2.3 on 2019-07-22 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20190722_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subject_dept_name', to='courses.Department'),
        ),
    ]
