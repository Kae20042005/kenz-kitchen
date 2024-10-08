# Generated by Django 5.1.1 on 2024-09-17 11:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_moodentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
