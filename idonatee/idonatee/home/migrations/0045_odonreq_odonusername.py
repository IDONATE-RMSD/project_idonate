# Generated by Django 4.0.6 on 2023-06-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_rdonreq_rdonusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='odonreq',
            name='odonusername',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
