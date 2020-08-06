# Generated by Django 2.2 on 2020-08-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('employment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('availability_date', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Consultant',
                'verbose_name_plural': 'Consultants',
            },
        ),
    ]
