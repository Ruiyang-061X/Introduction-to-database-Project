# Generated by Django 3.1.2 on 2020-10-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_film_comment_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image_path',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]