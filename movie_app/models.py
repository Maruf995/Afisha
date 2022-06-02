from django.db import models

STARS = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')


    @property
    def count_movies(self):
        return self.movies.all().count()
    # class Meta:
    #     verbose_name = 'Режиссер'
    #     verbose_name_plural = 'Режиссер'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    duration = models.TimeField(verbose_name='Продолжительность')
    director = models.ForeignKey('Director', on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = 'Кино'
    #     verbose_name_plural = 'Кино'

    def __str__(self):
        return self.title

    @property
    def rating(self):
        reviews = self.reviews.all()
        count = reviews.count()
        average = 0
        for i in reviews:
            average += i.stars
        try:
            return average / count
        except:
            return 0

    @property
    def filter_reviews(self):
        return [{'id': i.id, 'text': i.text, 'stars': i.stars}
                for i in self.reviews.filter(stars__gt=3)]


class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STARS, default=5)

    # class Meta:
    #     verbose_name = 'Обзор'
    #     verbose_name_plural = 'Обзор'

    def __str__(self):
        return self.movie.title
