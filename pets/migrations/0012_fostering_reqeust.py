# Generated by Django 5.0.3 on 2024-04-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0011_vacci_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fostering',
            name='Reqeust',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=100, null=True),
        ),
    ]
