# Generated by Django 4.1.1 on 2022-09-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('bmw', 'BMW'), ('jaguar', 'JAGAUR'), ('toyota', 'TOYOTA'), ('audi', 'AUDI'), ('renaulT', 'RENAULT')], max_length=20)),
            ],
        ),
    ]
