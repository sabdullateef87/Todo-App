# Generated by Django 5.0.4 on 2024-05-01 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateField(default='2024-05-01')),
                ('name', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2024-05-01')),
                ('due_date', models.DateField(default='2024-05-01')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
