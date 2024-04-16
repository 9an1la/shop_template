from django.db import models
# Create your models here.


class Category(models.Model):
    title = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['title']


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField('Название товара', max_length=100)
    manufacturer = models.CharField('Производитель', max_length=100)
    amount = models.IntegerField('Количество товара')
    price = models.IntegerField('Цена', default=0)
    prod_pict = models.ImageField('Фото товара', upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['amount']