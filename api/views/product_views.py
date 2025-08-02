from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from api.selectors.product_selectors import product_list
from api.services.product_services import product_update,product_delete
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsManager
class ProductListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
        price = serializers.DecimalField(max_digits=6, decimal_places=2)
        img = serializers.ImageField(required=False, allow_null=True)
        
    class FilterSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        price = serializers.DecimalField(required=False,max_digits=6, decimal_places=2)
        
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        price = serializers.DecimalField(required=False,max_digits=6, decimal_places=2)
        img = serializers.ImageField(required=False)
        
    def get (self, request):
        filters_serializer = self.FilterSerializer(data= request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        products_qs = product_list(filters=filters_serializer.validated_data)
        output_serializer = self.OutputSerializer(products_qs, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
    
class ProductUpdateOrDeleteApi(APIView):
    
    permission_classes=[IsAuthenticated,IsManager]
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        price = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)
        img = serializers.ImageField(required=False)
    
    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
        price = serializers.DecimalField( max_digits=6, decimal_places=2)
        img = serializers.ImageField(required=False)
    
    def put(self, request,pk):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        product = product_update(
            pk=pk,
            data=input_serializer.validated_data
        )
        output_serializer = self.OutputSerializer(product)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
    def delete(self,request,pk):
        product = product_delete(pk)
        if not product :
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(f"{product.name} deleted successfuly!!")

