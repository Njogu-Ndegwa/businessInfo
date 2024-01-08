# Generated by Django 5.0.1 on 2024-01-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30)),
                ('services_offered', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=30)),
                ('business_contact', models.CharField(max_length=30)),
                ('business_email', models.CharField(max_length=30)),
                ('social_media_handle', models.CharField(max_length=30)),
                ('business_website', models.CharField(max_length=30)),
                ('whatsup_link', models.CharField(max_length=30)),
            ],
        ),
    ]
