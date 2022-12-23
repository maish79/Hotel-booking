# Generated by Django 3.2.16 on 2022-12-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('single', 'one'), ('double', 'two'), ('family', 'multi')], max_length=6),
        ),
    ]