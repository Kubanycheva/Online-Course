# Generated by Django 5.1.3 on 2024-12-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0004_course_level_userprofile_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_en',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_ru',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='certificate_url_en',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='certificate_url_ru',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions_en',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions_ru',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_en',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_ru',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_en',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ru',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
