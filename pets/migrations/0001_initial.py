# Generated by Django 5.0.3 on 2024-03-20 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('species', models.CharField(blank=True, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird')], max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('adoptionFee', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PetPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.TextField(max_length=200, null=True)),
                ('bread', models.TextField(max_length=200, null=True)),
                ('size', models.CharField(blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=100, null=True)),
                ('ageRange', models.CharField(blank=True, choices=[('Puppy', 'Puppy'), ('Adult', 'Adult'), ('Senior', 'Senior')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeetAndGreet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('scheduledAt', models.DateTimeField(auto_now=True)),
                ('location', models.TextField(max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
        migrations.CreateModel(
            name='AdoptionApplication',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('submittedAt', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]