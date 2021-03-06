from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(Goods, verbose_name='商品', help_text='商品id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        # 联合唯一索引，映射数据库（数据库完成，数据库抛异常）
        unique_together = ('user', 'goods')  # 需要migration

    def __str__(self):
        return f"{self.user.username} - {self.goods.name}"


class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购'),
    )
    user = models.ForeignKey(User, verbose_name='用户')
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name='用户留言类型',
                                       help_text="""(1, '留言'),(2, '投诉'),(3, '询问'),(4, '售后'),(5, '求购')""")
    subject = models.CharField(max_length=100, default='', verbose_name='主题', help_text="主题")
    message = models.TextField(default='', verbose_name='留言内容',  help_text='留言内容')
    file = models.FileField(verbose_name='上传的文件', blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.name} - {self.message}"


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    province = models.CharField(max_length=100,  default='', verbose_name='省份')
    city = models.CharField(max_length=100, default='', verbose_name='城市')
    district = models.CharField(max_length=100, default='', verbose_name='区域')
    address = models.CharField(max_length=100, default='', verbose_name='收货地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.name} - {self.address}"

