# Generated by Django 2.1.5 on 2020-01-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0004_auto_20200102_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='predications',
            field=models.CharField(default='[[]]', max_length=2048),
        ),
    ]