# Generated by Django 5.0.2 on 2024-02-19 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.question')),
            ],
        ),
    ]
