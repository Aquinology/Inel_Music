# Generated by Django 3.1.6 on 2021-02-18 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Сценическое имя')),
                ('slug', models.SlugField(verbose_name='Идентификатор')),
                ('artist_pic', models.ImageField(blank=True, default='pictures/artists/default.jpg', upload_to='pictures/artists', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Жанр')),
                ('slug', models.SlugField(verbose_name='Идентификатор')),
                ('genre_pic', models.ImageField(blank=True, default='pictures/genres/default.jpg', upload_to='pictures/genres', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Идентификатор')),
                ('song_pic', models.ImageField(blank=True, default='pictures/songs/default.jpg', upload_to='pictures/songs', verbose_name='Картинка')),
                ('song', models.FileField(upload_to='tracks', verbose_name='Трек')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('size', models.IntegerField(default=0, verbose_name='Размер')),
                ('playtime', models.CharField(default='0.00', max_length=10, verbose_name='Продолжительность')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст песни')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('artists', models.ManyToManyField(to='music.Artist', verbose_name='Исполнители')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='music.genre', verbose_name='Жанр')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Композиция',
                'verbose_name_plural': 'Композиции',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Идентификатор')),
                ('album_pic', models.ImageField(blank=True, default='pictures/albums/default.jpg', upload_to='pictures/albums', verbose_name='Картинка')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('artists', models.ManyToManyField(to='music.Artist', verbose_name='Исполнители')),
                ('songs', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Композиции', to='music.song')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]
