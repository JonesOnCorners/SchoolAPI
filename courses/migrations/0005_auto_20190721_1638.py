# Generated by Django 2.2.2 on 2019-07-21 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190721_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_departments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Department'),
        ),
    ]