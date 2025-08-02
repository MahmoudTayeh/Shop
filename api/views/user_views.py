from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from api.selectors.user_selectors import customUser_list
from api.permissions import IsManager
from rest_framework.permissions import IsAuthenticated
from api.services.user_services import customUser_delete
# Create your views here.

class UserListApi(APIView):
    permission_classes=[IsAuthenticated,IsManager]
    class OutputSerializer(serializers.Serializer):
        username = serializers.CharField()
        email = serializers.EmailField()
        phone_number = serializers.CharField()
        created_at = serializers.DateTimeField()
    class FilterSerializer(serializers.Serializer):
        username = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
    def get (self, request):
        filters_serializer = self.FilterSerializer(data= request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        users_qs = customUser_list(filters=filters_serializer.validated_data)
        output_serializer = self.OutputSerializer(users_qs, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)

class UserDeleteApi(APIView):
    permission_classes=[IsAuthenticated,IsManager]
    
    def delete(self,request,pk):
        user =customUser_delete(pk)
        if not user:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(f"{user.username} deleted successfuly!! ", status=status.HTTP_200_OK)
        