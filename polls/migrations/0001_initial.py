# Generated by Django 5.1.4 on 2024-12-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=200)),
                ('email', models.TextField(max_length=200)),
                ('senha', models.TextField(max_length=500)),
            ],
        ),
    ]
