# Generated by Django 3.1.6 on 2021-02-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmeme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
