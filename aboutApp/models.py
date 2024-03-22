from django.db import models

class Award(models.Model):  # 荣誉模型
    description = models.TextField(max_length=500,
                               blank=True,
                               null=True,
                               verbose_name='景点描述')
    photo = models.ImageField(upload_to='Award/',
                            blank=True,
                            verbose_name='景点照片')

    class Meta:
        verbose_name = '景点'
        verbose_name_plural = '景点' 