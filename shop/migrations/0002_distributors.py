# Generated by Django 4.2.5 on 2023-09-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='shops/')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('contacts', models.PositiveIntegerField()),
            ],
        ),
    ]
