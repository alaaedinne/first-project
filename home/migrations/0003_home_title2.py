# Generated by Django 3.1.3 on 2020-12-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201202_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='title2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
