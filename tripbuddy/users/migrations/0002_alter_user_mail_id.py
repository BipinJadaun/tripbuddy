# Generated by Django 5.0.6 on 2024-05-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail_id',
            field=models.EmailField(max_length=50),
        ),
    ]
