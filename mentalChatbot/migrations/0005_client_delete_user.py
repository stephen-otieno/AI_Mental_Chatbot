# Generated by Django 5.1.3 on 2025-02-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalChatbot', '0004_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.CharField(max_length=100)),
                ('client_message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
