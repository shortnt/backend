# Generated by Django 4.0.3 on 2022-04-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textsumm', '0012_alter_manualuserdetails_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='filedetails',
            name='url_link',
            field=models.CharField(default='null', max_length=10000),
        ),
    ]