# Generated by Django 2.2.3 on 2019-07-29 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190723_0940'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
