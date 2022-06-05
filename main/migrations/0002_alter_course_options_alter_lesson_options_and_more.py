# Generated by Django 4.0.4 on 2022-05-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'دوره', 'verbose_name_plural': 'دوره'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'درس', 'verbose_name_plural': 'درس'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name': 'استاد', 'verbose_name_plural': 'استاد'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='classtime',
        ),
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.AddField(
            model_name='course',
            name='startdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='timeperiod',
            field=models.IntegerField(null=True, verbose_name='مدت زمان دوره (ساعت)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='main.teachers', verbose_name='استاد'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
    ]