# Generated by Django 3.2.8 on 2021-10-05 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0005_auto_20211005_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platenumber',
            name='plate_number_datafromhub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platenumber', to='datahub.datafromhub'),
        ),
    ]
