# Generated by Django 4.1.1 on 2023-11-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MailSender', '0006_alter_uploaded_file_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_file',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
