# Generated by Django 3.2.7 on 2021-09-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2021-09-23', max_length=20, verbose_name='出生日期'),
        ),
    ]
