# Generated by Django 5.0.7 on 2024-07-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
