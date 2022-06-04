# Generated by Django 4.0.4 on 2022-06-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_course_teacher_course_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=5000)),
            ],
        ),
        migrations.DeleteModel(
            name='lesson',
        ),
    ]
