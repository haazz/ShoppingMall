from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/product/category/{self.slug}'
    # admin 화면에서 Categorys를 Categories로 바꿔줌
    class Meta:
        verbose_name_plural = 'Categories'
class Product(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    def get_absolute_url(self):
        return f'/product/{self.pk}/'