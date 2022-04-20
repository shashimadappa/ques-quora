# Generated by Django 4.0.3 on 2022-04-19 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
