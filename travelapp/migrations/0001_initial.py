# Generated by Django 3.2.16 on 2023-01-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
