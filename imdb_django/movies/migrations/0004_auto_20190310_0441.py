# Generated by Django 2.1.5 on 2019-03-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190310_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='celebs',
            field=models.ManyToManyField(to='celebs.Celeb'),
        ),
    ]
