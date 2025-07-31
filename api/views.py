from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .selectors import customUser_list
# Create your views here.

class UserListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        phone_number = serializers.CharField()
        created_at = serializers.DateTimeField()
    class FilterSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
    def get (self, request):
        filters_serializer = self.FilterSerializer(data= request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        users_qs = customUser_list(filters=filters_serializer.validated_data)
        output_serializer = self.OutputSerializer(users_qs, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)