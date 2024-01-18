from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продукта:
    - название продукта
    - описание
    - изображение
    - категория продукта (ссылается на модель Category)
    - цена
    - дата создания
    - дата измененния
    - продавец (ссылается на модель User)
    - статус публикации (доступен для изменения только модератору сайта)
    """
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_of_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.id} {self.product_name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    """Модель категории продуктов:
    - название категории
    - описание
    """
    category_name = models.CharField(max_length=150, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    """Модель версии продукта:
    - пролукт (ссылается на модель Product)
    - номер версии
    - название версии
    - статус версии (активна/не активна)
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.SmallIntegerField(verbose_name='Версия')
    name = models.CharField(max_length=250, verbose_name='Название версии')
    is_activ = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} - {self.number} / {self.is_activ}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        unique_together = (('number', 'product'),)
