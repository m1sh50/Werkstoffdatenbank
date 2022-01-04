# Generated by Django 3.2.8 on 2022-01-02 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('werkstoffnummer', models.CharField(max_length=100)),
                ('werkstoffbezeichnung', models.CharField(max_length=100)),
                ('gruppe', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('Iron_Fe', models.CharField(blank=True, default='', max_length=100)),
                ('Carbon_C', models.CharField(blank=True, default='', max_length=100)),
                ('Cobalt_Co', models.CharField(blank=True, default='', max_length=100)),
                ('Nickel_Ni', models.CharField(blank=True, default='', max_length=100)),
                ('Copper_Cu', models.CharField(blank=True, default='', max_length=100)),
                ('Zinc_Zn', models.CharField(blank=True, default='', max_length=100)),
                ('Mananese_Mn', models.CharField(blank=True, default='', max_length=100)),
                ('Chromuium_Cr', models.CharField(blank=True, default='', max_length=100)),
                ('Vanadium_V', models.CharField(blank=True, default='', max_length=100)),
                ('Titaniun_Ti', models.CharField(blank=True, default='', max_length=100)),
                ('Cadmium_Cd', models.CharField(blank=True, default='', max_length=100)),
                ('Silver_Ag', models.CharField(blank=True, default='', max_length=100)),
                ('Palladium_Pb', models.CharField(blank=True, default='', max_length=100)),
                ('Rhodium_Rh', models.CharField(blank=True, default='', max_length=100)),
                ('Molydbenum_Mo', models.CharField(blank=True, default='', max_length=100)),
                ('Niobium_Nb', models.CharField(blank=True, default='', max_length=100)),
                ('Zirconium_Zr', models.CharField(blank=True, default='', max_length=100)),
                ('Yttrium_Y', models.CharField(blank=True, default='', max_length=100)),
                ('Tungesten_W', models.CharField(blank=True, default='', max_length=100)),
                ('Aluminium_Al', models.CharField(blank=True, default='', max_length=100)),
                ('Boron_B', models.CharField(blank=True, default='', max_length=100)),
                ('Gallium_Ga', models.CharField(blank=True, default='', max_length=100)),
                ('Indium_In', models.CharField(blank=True, default='', max_length=100)),
                ('Lead_Pb', models.CharField(blank=True, default='', max_length=100)),
                ('Silicon_Si', models.CharField(blank=True, default='', max_length=100)),
                ('Tin_Sn', models.CharField(blank=True, default='', max_length=100)),
                ('Nitrogen_N', models.CharField(blank=True, default='', max_length=100)),
                ('Phosphorus_P', models.CharField(blank=True, default='', max_length=100)),
                ('Sulfur_S', models.CharField(blank=True, default='', max_length=100)),
                ('Notes', models.CharField(blank=True, default='', max_length=5000)),
                ('Technetium_Tc', models.CharField(blank=True, default='', max_length=100)),
                ('Hardness_HV', models.CharField(blank=True, default='', max_length=1000)),
                ('Hardness_HRC', models.CharField(blank=True, default='', max_length=1000)),
                ('Hardness_HBW', models.CharField(blank=True, default='', max_length=1000)),
                ('files_Hardness', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('Tensile_Strength_Rm', models.CharField(blank=True, default='', max_length=1000)),
                ('Streckgrenze_Rp', models.CharField(blank=True, default='', max_length=1000)),
                ('Streckgrenze_ReH', models.CharField(blank=True, default='', max_length=1000)),
                ('Streckgrenze_ReL', models.CharField(blank=True, default='', max_length=1000)),
                ('Tensile_Stretch_A', models.CharField(blank=True, default='', max_length=1000)),
                ('Gleichmaßdehnung_Ag', models.CharField(blank=True, default='', max_length=1000)),
                ('files_Tensile', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('Kerbschlagarbeit', models.CharField(blank=True, default='', max_length=1000)),
                ('Temperatur', models.CharField(blank=True, default='', max_length=1000)),
                ('files_Charpy', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('EModul', models.CharField(blank=True, default='', max_length=1000)),
                ('files_Modulus', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('Density', models.CharField(blank=True, default='', max_length=100)),
                ('files_Density', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('Probe', models.CharField(blank=True, default='', max_length=1000)),
                ('Gefüge_Beschreibung', models.CharField(blank=True, default='', max_length=1000)),
                ('files_Metallo', models.FileField(blank=True, default='no_data.html', upload_to='chapters/%Y/%m/%D')),
                ('Wärmebehandlung', models.CharField(blank=True, default='', max_length=1000)),
                ('Ätzung', models.CharField(blank=True, default='', max_length=1000)),
                ('Gefüge_Aufnhame', models.ImageField(blank=True, default='no_data.jpg', upload_to='chapters/%Y/%m/%D')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
