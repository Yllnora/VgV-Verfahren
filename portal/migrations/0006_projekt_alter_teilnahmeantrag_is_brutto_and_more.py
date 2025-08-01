# Generated by Django 4.2.21 on 2025-05-25 20:54

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_teilnahmeantrag_is_brutto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('beschreibung', models.TextField(blank=True)),
                ('deadline', models.DateField(default=django.utils.timezone.now, help_text='Abgabefrist für dieses Projekt')),
            ],
        ),
        migrations.AlterField(
            model_name='teilnahmeantrag',
            name='is_brutto',
            field=models.BooleanField(default=True, help_text='Ankreuzen, wenn der Umsatz Brutto (inkl. Steuer) angegeben ist.'),
        ),
        migrations.AlterField(
            model_name='teilnahmeantrag',
            name='steuer_satz',
            field=models.DecimalField(decimal_places=2, default=Decimal('19.00'), help_text='Steuersatz in Prozent (z. B. 19.00 für 19%).', max_digits=5),
        ),
        migrations.AddField(
            model_name='teilnahmeantrag',
            name='projekt',
            field=models.ForeignKey(blank=True, help_text='Für welches Projekt reichen Sie diesen Antrag ein?', null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.projekt'),
        ),
    ]
