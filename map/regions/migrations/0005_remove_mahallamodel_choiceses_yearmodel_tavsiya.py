# Generated by Django 4.2.6 on 2023-10-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0004_mahallamodel_choiceses_alter_yearmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahallamodel',
            name='choiceses',
        ),
        migrations.AddField(
            model_name='yearmodel',
            name='tavsiya',
            field=models.TextField(blank=True, null=True),
        ),
    ]
