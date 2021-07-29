# Generated by Django 3.2.5 on 2021-07-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210728_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='stat_defensa',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jugador',
            name='stat_fuerza',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jugador',
            name='stat_resistencia',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jugador',
            name='stat_velocidad',
            field=models.IntegerField(default=1),
        ),
    ]
