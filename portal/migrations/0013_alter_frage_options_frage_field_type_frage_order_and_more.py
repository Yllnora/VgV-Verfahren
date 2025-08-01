# Generated by Django 4.2.21 on 2025-06-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_frage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='frage',
            name='field_type',
            field=models.CharField(choices=[('boolean', 'Ja/Nein'), ('text', 'Freitext')], default='boolean', max_length=20),
        ),
        migrations.AddField(
            model_name='frage',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Reihenfolge der Fragen in Formular'),
        ),
        migrations.AddField(
            model_name='teilnahmeantrag',
            name='antworten',
            field=models.JSONField(blank=True, default=dict, help_text='Speichert die Antworten auf projektspezifische Fragen als JSON'),
        ),
        migrations.AlterField(
            model_name='frage',
            name='text',
            field=models.TextField(help_text="Die Fragestellung, z.B. 'Gab es besondere Anforderungen?'"),
        ),
    ]
