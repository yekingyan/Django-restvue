from rest_framework import serializers

from goods.models import Goods


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()

    def create(self, validated_data):
        # 写入满足上面类变量的validate_data到数据库
        return Goods.objects.create(**validated_data)
