# Generated by Django 3.1.3 on 2020-12-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Home'},
        ),
        migrations.AddField(
            model_name='home',
            name='inder1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]