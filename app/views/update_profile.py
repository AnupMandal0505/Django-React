from django.shortcuts import render,redirect
from django.views import View
from app.models import User
import random
# from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from datetime import datetime

from rest_framework import status

from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from app.serializers.userSerializer import UserSerializer
from app.serializers.UpdateProfileSerializer import UpdateProfileSerializer


@permission_classes([IsAuthenticated]) 
class UpdateProfileAPI(APIView):
    def put(self, request):
        try:
        
            serializer = UpdateProfileSerializer(data=request.data)
            if serializer.is_valid():

                User.objects.filter(user_id=request.user).update(**serializer.validated_data)
                responseData=User.objects.filter(user_id=request.user).first()

                responseData= UpdateProfileSerializer(responseData,many=False).data
                return Response(responseData,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_response = {
                'status': 400,
                'error': 'something_went_wrong',
                'message': 'Not Update',
                'data': {}
            }
            return Response(error_response, status=400)
        



