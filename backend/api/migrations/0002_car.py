# Generated by Django 5.0.2 on 2024-02-10 08:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='api.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]