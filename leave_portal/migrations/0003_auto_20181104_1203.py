# Generated by Django 2.1.3 on 2018-11-04 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave_portal', '0002_auto_20181104_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applyleave',
            old_name='Flag',
            new_name='flag',
        ),
    ]