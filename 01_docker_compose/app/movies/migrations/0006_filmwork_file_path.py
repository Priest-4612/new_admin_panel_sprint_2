# Generated by Django 3.2 on 2022-05-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20220508_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='data/movies/', verbose_name='file'),
        ),
    ]
