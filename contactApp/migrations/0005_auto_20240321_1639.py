# Generated by Django 2.2.4 on 2024-03-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0004_auto_20240320_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2024-03-21', max_length=20, verbose_name='出生日期'),
        ),
    ]
