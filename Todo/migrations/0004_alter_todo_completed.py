# Generated by Django 5.0.6 on 2024-06-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]