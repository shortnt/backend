# Generated by Django 4.0 on 2021-12-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textsumm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicksummary',
            name='Output',
            field=models.CharField(default='null', max_length=1000000),
        ),
    ]
