# Generated by Django 2.2 on 2020-08-04 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benchlist', '0004_consultant_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BenchConsultant',
            new_name='Benchlist',
        ),
        migrations.AlterModelOptions(
            name='benchlist',
            options={'verbose_name': 'Benchlist', 'verbose_name_plural': 'Benchlist consultants'},
        ),
    ]