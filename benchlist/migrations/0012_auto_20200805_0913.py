# Generated by Django 2.2 on 2020-08-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchlist', '0011_submission_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
