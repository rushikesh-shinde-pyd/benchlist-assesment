# Generated by Django 2.2 on 2020-08-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchlist', '0010_auto_20200805_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='note',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]
