# Generated by Django 2.1 on 2018-11-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationerror',
            name='method',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
