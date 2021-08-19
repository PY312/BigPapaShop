from django.db import models


# Create your models here.
class Category(models.Model):
    # Категории
    name = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField('Теги', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Product(models.Model):
    # Товары
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField('Изображение', upload_to='static/images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название товара"
        verbose_name_plural = "Название товаров"
