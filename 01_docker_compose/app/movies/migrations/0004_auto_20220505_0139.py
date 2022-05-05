# Generated by Django 3.2 on 2022-05-04 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220505_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmworkgenre',
            name='film_work',
            field=models.ForeignKey(db_column='film_work_id', on_delete=django.db.models.deletion.CASCADE, related_name='film_work_genres', to='movies.filmwork', verbose_name='film_work'),
        ),
        migrations.AlterField(
            model_name='filmworkgenre',
            name='genre',
            field=models.ForeignKey(db_column='genre_id', on_delete=django.db.models.deletion.CASCADE, related_name='film_work_genres', to='movies.genre', verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='filmworkperson',
            name='film_work',
            field=models.ForeignKey(db_column='film_work_id', on_delete=django.db.models.deletion.CASCADE, related_name='film_work_persons', to='movies.filmwork', verbose_name='film_work'),
        ),
        migrations.AlterField(
            model_name='filmworkperson',
            name='person',
            field=models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, related_name='film_work_persons', to='movies.person', verbose_name='person'),
        ),
    ]