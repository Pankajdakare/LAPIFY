# Generated by Django 5.0.3 on 2024-03-10 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='la_image1',
            field=models.ImageField(default='', upload_to='image'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='la_image2',
            field=models.ImageField(default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='details',
            field=models.CharField(max_length=3000),
        ),
    ]
