# Generated by Django 4.2.1 on 2023-05-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('game_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, unique=True, verbose_name='Название игры')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('buy', models.BooleanField(default=False, help_text='Куплена игра или нет', verbose_name='Куплена')),
                ('beta', models.BooleanField(default=False, help_text='Игра находится в бета тестировании или нет', verbose_name='Игра в бете')),
                ('passed', models.BooleanField(default=False, help_text='Игра пройдена или нет', verbose_name='Игра пройдена')),
                ('publisher', models.CharField(blank=True, max_length=70, null=True, verbose_name='Издатель')),
                ('developer', models.CharField(blank=True, max_length=70, null=True, verbose_name='Разработчик')),
                ('game_platform', models.ManyToManyField(blank=True, to='game_platform.gameplatformmodel')),
                ('genres', models.ManyToManyField(blank=True, to='genre.gamegenremodel')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
