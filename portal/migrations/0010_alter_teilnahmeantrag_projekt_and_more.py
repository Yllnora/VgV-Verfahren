# Generated by Django 4.2.21 on 2025-06-01 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_alter_projekt_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teilnahmeantrag',
            name='projekt',
            field=models.ForeignKey(default=3, help_text='Für welches Projekt reichen Sie diesen Antrag ein?', on_delete=django.db.models.deletion.PROTECT, to='portal.projekt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teilnahmeantrag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
