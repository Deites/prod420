# Generated by Django 3.2.8 on 2021-10-05 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0007_alter_platenumber_plate_number_datafromhub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platenumber',
            name='plate_number_datafromhub',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datahub.datafromhub'),
        ),
    ]
