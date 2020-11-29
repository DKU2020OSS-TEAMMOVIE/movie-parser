# Generated by Django 2.2.11 on 2020-11-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20201121_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBTI',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4, unique=True)),
                ('genres', models.ManyToManyField(to='myapp.Genre')),
            ],
        ),
    ]
