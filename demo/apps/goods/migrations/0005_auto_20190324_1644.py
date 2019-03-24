# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-24 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20190313_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(help_text='商品类目', on_delete=django.db.models.deletion.CASCADE, related_name='indexAd', to='goods.GoodsCategory', verbose_name='商品类目')),
                ('goods', models.ForeignKey(help_text='商品类目', on_delete=django.db.models.deletion.CASCADE, related_name='indexAd', to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, help_text='商品类目', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
