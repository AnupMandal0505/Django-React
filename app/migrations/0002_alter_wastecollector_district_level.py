# Generated by Django 4.0 on 2024-01-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastecollector',
            name='district_level',
            field=models.CharField(blank=True, choices=[('Dhanbad', 'Dhanbad'), ('Bokaro', 'Bokaro'), ('None', 'None')], max_length=20, null=True),
        ),
    ]
