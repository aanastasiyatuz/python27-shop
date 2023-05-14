from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		exclude = ("order",)


class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
	items = OrderItemSerializer(many=True)

	class Meta:
		model = Order
		fields = ("user", "is_paid", "created_at", "total_price", "items")
