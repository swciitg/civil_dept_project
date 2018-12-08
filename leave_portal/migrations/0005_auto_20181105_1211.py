# Generated by Django 2.1.3 on 2018-11-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_portal', '0004_auto_20181105_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Acedemic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Maternity',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Paternity',
        ),
        migrations.AddField(
            model_name='student',
            name='conference',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='student',
            name='sample_Collection',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='applyleave',
            name='TypeOfLeave',
            field=models.CharField(choices=[('Ordinary', 'Ordinary'), ('Medical', 'Medical'), ('Conference', 'Conference'), ('Sample Collection', 'Sample Collection')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, choices=[('Mtech', 'Mtech'), ('Phd', 'Phd')], max_length=128),
        ),
    ]