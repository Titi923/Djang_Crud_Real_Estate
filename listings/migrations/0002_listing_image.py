# Generated by Django 4.1.7 on 2023-02-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
