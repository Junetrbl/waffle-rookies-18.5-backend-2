# Generated by Django 3.1 on 2020-09-27 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('participant', 'participant'), ('instructor', 'instructor')], max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='userauth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userauth',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.auth'),
        ),
    ]
