# Generated by Django 3.2.6 on 2021-09-07 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='title',
            new_name='product',
        ),
        migrations.AddField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/variations/'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
