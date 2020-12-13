# Generated by Django 3.1.4 on 2020-12-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_data', models.DateTimeField(verbose_name='Last Updated')),
                ('body_text', models.TextField(blank=True, verbose_name='Page content')),
            ],
        ),
    ]
