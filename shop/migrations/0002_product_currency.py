# Generated by Django 2.0.6 on 2018-06-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(default='&#8373;', max_length=50),
        ),
    ]
