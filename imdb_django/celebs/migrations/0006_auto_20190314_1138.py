# Generated by Django 2.1.7 on 2019-03-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0005_auto_20190314_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='celeb',
            name='avatar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='celeb',
            unique_together=set(),
        ),
    ]