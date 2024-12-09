# Generated by Django 5.1.3 on 2024-12-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0003_review_comment_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('начальный', 'начальный'), ('средний', 'средний'), ('продвинутый', 'продвинутый')], default='начальный', max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_role',
            field=models.CharField(choices=[('клиент', 'клиент'), ('преподаватель', 'преподаватель'), ('администратор', 'администратор')], default='клиент', max_length=16),
        ),
    ]