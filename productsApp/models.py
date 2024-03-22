from django.db import models
from django.utils import timezone

class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('一日游', '一日游'),
        ('多日游', '多日游'),
        ('亲子游', '亲子游'),
    )
    title = models.CharField(max_length=50, verbose_name=' 标题')
    description = models.TextField(verbose_name='详情描述')
    productType = models.CharField(choices=PRODUCTS_CHOICES,
                                   max_length=50,
                                   verbose_name='类型')
    price = models.DecimalField(max_digits=7,
                                decimal_places=1,
                                blank=True,
                                null=True,
                                verbose_name='价格')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '旅游团'
        verbose_name_plural = '旅游团'
        ordering = ('-publishDate', )


class ProductImg(models.Model):
    product = models.ForeignKey(Product,
                                related_name='productImgs',
                                verbose_name='旅游团',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Product/',
                              blank=True,
                              verbose_name='图片')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
