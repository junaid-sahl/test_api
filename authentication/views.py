from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from authentication.models import UserAccount
from authentication.serializers import UsersSerializer


class UsersListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        plan = UserAccount.objects.all()
        serializer = UsersSerializer(plan, many=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Users List',
            'data': serializer.data
        }
        return Response(response)


class InsertUsersAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User Account Insertion Successful',
            'data': []
        }
        print(request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response['data'] = serializer.data
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
