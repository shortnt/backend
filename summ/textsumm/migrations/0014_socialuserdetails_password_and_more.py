# Generated by Django 4.0.3 on 2022-04-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textsumm', '0013_filedetails_url_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuserdetails',
            name='password',
            field=models.CharField(default='null', max_length=1000),
        ),
        migrations.AlterField(
            model_name='socialuserdetails',
            name='image',
            field=models.CharField(default='https://i.picsum.photos/id/509/200/200.jpg?hmac=F3VucjvZ_2eEx_ObPM7NJ_Ymq5jESSGCuXo_8japTZc', max_length=1000),
        ),
    ]
