# from rest_framework import serializers
# from .models import Product, CartItem, Cart, Collection
# from django.contrib.auth.models import User

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()

#     class Meta:
#         model = CartItem
#         fields = ['product', 'amount']

# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True)

#     class Meta:
#         model = Cart
#         fields = ['id', 'items']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# class CollectionSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True)

#     class Meta:
#         model = Collection
#         fields = '__all__'

# ! fdsfdsf

from rest_framework import serializers
from .models import Product, CartItem, Cart, Collection
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'amount']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CollectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Collection
        fields = '__all__'
