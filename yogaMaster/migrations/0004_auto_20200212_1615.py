# Generated by Django 2.2.5 on 2020-02-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogaMaster', '0003_auto_20200210_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='compareImg',
            field=models.ImageField(upload_to='yogaMaster/images/result'),
        ),
        migrations.AlterField(
            model_name='result',
            name='uploadImg',
            field=models.ImageField(upload_to='yogaMaster/images/upload'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usrProfile',
            field=models.ImageField(upload_to='yogaMaster/images/avater'),
        ),
        migrations.AlterField(
            model_name='yogaimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
