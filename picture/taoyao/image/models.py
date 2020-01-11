from django.db import models

# Create your models here.
class Picture_Type(models.Model):
    p_type = models.CharField(max_length=50)
    class Meta:
        db_table = 'picture_type'

    def __str__(self):
        return str(self.p_type)


class Picture(models.Model):
    url = models.ImageField(verbose_name='图片路径')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    browse_count = models.IntegerField(default=0, verbose_name='浏览次数')
    picture_type = models.ForeignKey(Picture_Type)
    class Meta:
        db_table = 'Picture'
        verbose_name = '图片信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '%s %s '%(self.url,self.browse_count)

