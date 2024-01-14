from django.db import models


class Blog(models.Model):
    """Модель Блога:
    - blog_title: Заголовок
    - slug: Слаг
    - blog_content: Содержимое
    - blog_image: Превью
    - date_of_creation: Дата создания
    - publication_sign: Статус публикации
    - view_count: Счетчик просмотров
    """
    blog_title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    blog_content = models.TextField(verbose_name='Содержимое')
    blog_image = models.ImageField(upload_to='blog_image/', verbose_name='Превью', blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return (f'Заголовок - {self.blog_title}'
                f'Дата создания - {self.date_of_creation}'
                f'Опубликовано - {self.publication_sign}'
                f'Количество просмотров - {self.view_count}')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
