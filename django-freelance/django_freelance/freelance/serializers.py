from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ExecutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Executor
        fields = '__all__'

class CRUDExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

class CRUDCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    service_type = serializers.CharField(source='get_service_type_display')
    class Meta:
        model = Service
        fields = '__all__'

class CRUDServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_type = serializers.CharField(source='get_order_type_display')
    class Meta:
        model = Order
        fields = '__all__'

class CRUDOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    order = OrderSerializer

    class Meta:
        model = Tag
        fields = '__all__'

class CRUDTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class OrderingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    service = ServiceSerializer()
    order = OrderSerializer()
    class Meta:
        model = Ordering
        fields = '__all__'

class CRUDOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Message
        fields = '__all__'

class CRUDMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    severity = serializers.CharField(source='get_severity_display')
    class Meta:
        model = Ticket
        fields = '__all__'

class CRUDTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AuthoringSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    review = ReviewSerializer()
    author = UserSerializer()
    class Meta:
        model = Authoring
        fields = '__all__'

class CRUDAuthoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authoring
        fields = '__all__'
