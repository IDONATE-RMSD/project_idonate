# Generated by Django 4.0.6 on 2023-06-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_hrecreq_hrecusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='horgreq',
            name='horgusername',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]