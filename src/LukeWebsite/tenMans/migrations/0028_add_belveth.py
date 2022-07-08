from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenMans', '0027_alter_gamelanerstats_goldearned'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                "INSERT INTO tenMans_champion (championName, riotName) VALUES (\"Bel'veth\", \"Belveth\")",
            ],
            reverse_sql=[
                "DELETE from tenMans_champion WHERE riotName=\"Belveth\""
            ]
        )
    ]
