# Generated by Django 2.1.5 on 2019-03-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('cate_name',),
            },
        ),
    ]
