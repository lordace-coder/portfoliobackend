# Generated by Django 4.1.5 on 2023-02-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_messages',
            name='malicious_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
