# Generated by Django 4.2.2 on 2023-07-05 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_image_name_post_image_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_field',
            new_name='image',
        ),
    ]