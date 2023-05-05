# Generated by Django 4.2.1 on 2023-05-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlatformModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40, verbose_name='Название платформы')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание платформы')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]