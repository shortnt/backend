# Generated by Django 4.0 on 2021-12-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuickSummary',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Input', models.CharField(max_length=1000000)),
                ('Output', models.CharField(max_length=1000000)),
            ],
        ),
    ]
