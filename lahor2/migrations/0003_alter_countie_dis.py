# Generated by Django 3.2.6 on 2021-08-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lahor2', '0002_countie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countie',
            name='dis',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]