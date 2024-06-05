# Generated by Django 5.0.4 on 2024-05-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('topic', models.TextField(max_length=50)),
                ('desc', models.TextField(max_length=200)),
                ('thought_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
    ]