from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from api.selectors.order_selectors import order_list

class OrderListApi(APIView):
    class OrderItemSerializer(serializers.Serializer):
        product_name = serializers.CharField(source='product.name')
        quantity = serializers.IntegerField()
        price_at_time = serializers.DecimalField(max_digits=6, decimal_places=2)
    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        user = serializers.CharField(source='user.email')
        
        
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        user = serializers.CharField(source='user.email')
        created_at = serializers.DateTimeField()
        is_completed = serializers.BooleanField()
        items = OrderItemSerializer(many=True)

    def get(self, request) :
        filters_serializer = self.FilterSerializer(data = request.data)
        filters_serializer.is_valid(raise_exception=True)
        
        orders_qs = order_list(filters=filters_serializer.validated_data)
        output_serializer = self.OutputSerializer(orders_qs, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)

