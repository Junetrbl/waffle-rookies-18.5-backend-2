# Generated by Django 3.1 on 2020-09-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200928_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorprofile',
            name='year',
            field=models.SmallIntegerField(null=True),
        ),
    ]
