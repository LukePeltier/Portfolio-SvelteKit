# Generated by Django 3.2.5 on 2021-07-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenMans', '0017_auto_20210421_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderboardName', models.TextField(unique=True)),
                ('leaderboardValueName', models.TextField()),
                ('leaderboardEmoji', models.TextField()),
                ('leaderboardIsLifetime', models.BooleanField()),
            ],
        ),
    ]
