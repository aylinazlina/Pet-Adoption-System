# Generated by Django 5.0.3 on 2024-04-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_petpreference_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petpreference',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
