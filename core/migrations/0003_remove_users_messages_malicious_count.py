# Generated by Django 4.1.5 on 2023-02-16 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_users_messages_malicious_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_messages',
            name='malicious_count',
        ),
    ]
