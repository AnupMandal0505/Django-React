from django.shortcuts import render,redirect,HttpResponse
import random
# from app.models import Patient,Appointment,Department
from django.contrib import messages
from app.models import User,WasteCollector,DistrictPosition,StatePosition

from rest_framework.views import APIView
   
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from app.serializers.userSerializer import UserSerializer,UserWasteCollectorSerializer,UserDistrictCollectorSerializer,UserStateCollectorSerializer

import json
from urllib.parse import unquote



def getUserByType(user_ref, filter):

    print("filter",filter)
    condition = filter.pop('cond', None)
    print("condition",condition)
    print("filter",filter)

    USER = {
        "user_type":"USER"
    }
    ResponseData = []
    

    if "DWC" == condition:
        data=StatePosition.objects.get(user_ref=user_ref) 
        print("data",data)   
        state_level=data.state_level
        print("state_level",state_level)
        # UserDistrictCollectorSerializer
        DWCdata = UserDistrictCollectorSerializer(DistrictPosition.objects.filter(state=state_level, **filter), many=True)
        ResponseData += DWCdata.data
    elif "WC" == condition:
        if "SWC" == user_ref.user_type:
            data=StatePosition.objects.get(user_ref=user_ref)    
            state_level=data.state_level
            # UserWasteCollectorSerializer
            WCdata = UserWasteCollectorSerializer(WasteCollector.objects.filter(state=state_level, **filter), many=True)
            ResponseData += WCdata.data
        elif "DWC" == user_ref.user_type:
            data=DistrictPosition.objects.filter(user_ref=user_ref)    
            district_level=data.district_level
            WCdata = UserWasteCollectorSerializer(WasteCollector.objects.filter(district_level=district_level, **filter), many=True)
            ResponseData += WCdata.data

    else:

        # UserSerializer with ListSerializer
        user_list = User.objects.filter(**USER, **filter)
        print(user_list)
        Userdata = UserSerializer(user_list, many=True)
        ResponseData += list(Userdata.data)

    return ResponseData

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetUserALL(request):
    try:
        # print("params",type(request.query_params.get("name")))
        # Get the encoded filter from the query parameters
        encoded_filter = request.query_params.get('filter', None)
        decoded_filter = {}
        try:
            # Decode and parse the JSON filter
            decoded_filter = json.loads(unquote(encoded_filter))
        except:
            decoded_filter = {}

        print("decoded_filter",decoded_filter)

        # Check if the decoded filter is a dictionary
        if not isinstance(decoded_filter, dict):
            decoded_filter={}
        print(request.user)
        ResponseData=getUserByType(request.user,decoded_filter)
        return Response(ResponseData)
    
    except Exception as e:
        print("Error", e)
        error_response = {
            'status': 500,
            'error': 'something_went_wrong',
            'message': 'Internal server error',
            'data': {}
        }
        return Response(error_response, status=500)





# @permission_classes([IsAuthenticated]) 
# class GetUser(APIView):
#     def get(self, request):
#         try:
#             # print("params",type(request.query_params.get("name")))
#             # Get the encoded filter from the query parameters
#             encoded_filter = request.query_params.get('filter', None)
#             decoded_filter = {}
#             print("1",decoded_filter)
#             try:
#                 # Decode and parse the JSON filter
#                 decoded_filter = json.loads(unquote(encoded_filter))
#                 print("2",decoded_filter)
#             except:
#                 decoded_filter = {}
#                 print("3",decoded_filter)



#             # Check if the decoded filter is a dictionary
#             if not isinstance(decoded_filter, dict):
#                 decoded_filter={}
#                 print("4",decoded_filter)
            
#              # Filter based on the decoded filter
#             data_queryset = User.objects.filter(**decoded_filter)

#             # Serialize the queryset
#             serializer = UserSerializer(data=data_queryset, many=True)
#             serializer.is_valid()  # Call .is_valid() before accessing .data
#             serialized_data = serializer.data  # Access the serialized data

#             # Print or do something with the serialized data

#             return Response({"message": serialized_data})
     
#         except Exception as e:
#             print("Error", e)
#             error_response = { 
#                 'status': 500,
#                 'error': 'something_went_wrong',
#                 'message': 'Internal server error',
#                 'data': {}
#             }
#             return Response(error_response, status=500)
    


# @permission_classes([IsAuthenticated]) 
# class GetWasteCollector(APIView):
#     def get(self, request):
#         try:
#             # print("params",type(request.query_params.get("name")))
#             # Get the encoded filter from the query parameters
#             encoded_filter = request.query_params.get('filter', None)
#             decoded_filter = {}
#             print("1",decoded_filter)
#             try:
#                 # Decode and parse the JSON filter
#                 decoded_filter = json.loads(unquote(encoded_filter))
#                 print("2",decoded_filter)
#             except:
#                 decoded_filter = {}
#                 print("3",decoded_filter)



#             # Check if the decoded filter is a dictionary
#             if not isinstance(decoded_filter, dict):
#                 decoded_filter={}
#                 print("4",decoded_filter)
            
#              # Filter based on the decoded filter
#             data_queryset = WasteCollector.objects.filter(**decoded_filter)

#             # Serialize the queryset
#             serializer = UserWasteCollectorSerializer(data=data_queryset, many=True)
#             serializer.is_valid()  # Call .is_valid() before accessing .data
#             serialized_data = serializer.data  # Access the serialized data

#             # Print or do something with the serialized data

#             return Response({"message": serialized_data})
     
#         except Exception as e:
#             print("Error", e)
#             error_response = { 
#                 'status': 500,
#                 'error': 'something_went_wrong',
#                 'message': 'Internal server error',
#                 'data': {}
#             }
#             return Response(error_response, status=500)
    

# @permission_classes([IsAuthenticated]) 
# class GetDistrictWasteCollector(APIView):
#     def get(self, request):
#         try:
#             # print("params",type(request.query_params.get("name")))
#             # Get the encoded filter from the query parameters
#             encoded_filter = request.query_params.get('filter', None)
#             decoded_filter = {}
#             print("1",decoded_filter)
#             try:
#                 # Decode and parse the JSON filter
#                 decoded_filter = json.loads(unquote(encoded_filter))
#                 print("2",decoded_filter)
#             except:
#                 decoded_filter = {}
#                 print("3",decoded_filter)



#             # Check if the decoded filter is a dictionary
#             if not isinstance(decoded_filter, dict):
#                 decoded_filter={}
#                 print("4",decoded_filter)
            
#              # Filter based on the decoded filter
#             data_queryset = DistrictPosition.objects.filter(**decoded_filter)

#             # Serialize the queryset
#             serializer = UserDistrictCollectorSerializer(data=data_queryset, many=True)
#             serializer.is_valid()  # Call .is_valid() before accessing .data
#             serialized_data = serializer.data  # Access the serialized data

#             # Print or do something with the serialized data

#             return Response({"message": serialized_data})
     
#         except Exception as e:
#             print("Error", e)
#             error_response = { 
#                 'status': 500,
#                 'error': 'something_went_wrong',
#                 'message': 'Internal server error',
#                 'data': {}
#             }
#             return Response(error_response, status=500)
    
