# Generated by Django 5.0.2 on 2024-03-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_completed_remove_task_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TO DO', 'To Do'), ('IN PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TO DO', max_length=20),
        ),
    ]
