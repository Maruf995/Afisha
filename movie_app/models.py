from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссер'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    duration = models.TimeField(verbose_name='Продолжительность')
    director = models.ForeignKey('Director', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзор'

    def __str__(self):
        return self.movie.title
