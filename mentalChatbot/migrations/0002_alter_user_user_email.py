# Generated by Django 5.1.3 on 2025-02-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalChatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
