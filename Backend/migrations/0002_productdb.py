# Generated by Django 4.2.6 on 2023-11-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('ProductName', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to='product image')),
            ],
        ),
    ]
