# Generated by Django 3.1.3 on 2020-12-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_home_title3'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='inder3',
            field=models.TextField(default='', max_length=50),
            preserve_default=False,
        ),
    ]