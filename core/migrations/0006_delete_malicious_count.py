# Generated by Django 4.1.7 on 2023-03-03 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_users_messages_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Malicious_count',
        ),
    ]
