# Generated by Django 2.2.11 on 2020-11-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_movieuser_score_avg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieuser',
            name='score_avg',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
