# Generated by Django 5.0.7 on 2024-07-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_remove_alert_symbol_alert_email_alert_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='alert',
            name='title',
            field=models.CharField(default='Bitcoin', max_length=100),
        ),
    ]
