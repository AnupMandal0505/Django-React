from django.shortcuts import render,redirect
from django.views import View
from app.models import CollectionPoint,WasteCollector,StatePosition,DistrictPosition
import random
from rest_framework.permissions import IsAuthenticated

# from django.http import JsonResponse, HttpResponse

from datetime import datetime

from rest_framework import status

from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from app.serializers.userSerializer import UserSerializer

from django.core.mail import send_mail,EmailMultiAlternatives
# from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

from app.serializers.WasteCollectionPointSerializer import WasteCollectionPointSerializer
from django.shortcuts import get_object_or_404

import json
from urllib.parse import unquote


def unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=CollectionPoint.objects.get(collection_point_id=uq)
        except:
            return uq
        
@permission_classes([IsAuthenticated]) 
class WasteCollectionPointAPI(APIView):
    def post(self, request):
        if "USER" == request.user.user_type:
            try:
                address=request.data.get('address')
                locality=request.data.get('locality')
                district=request.data.get('district')
                pincode=request.data.get('pincode')
                state=request.data.get('state')
                country=request.data.get('country')
                lattitude=request.data.get('lattitude')
                longitude=request.data.get('longitude')

                customer_ref=request.user
                collection_point_id=unique_number("coll")
                ab = CollectionPoint.objects.create(customer_ref=customer_ref,collection_point_id=collection_point_id,optional_phone="none",address=address,locality=locality,district=district,pincode=pincode,state=state,country=country,lattitude=lattitude,longitude=longitude)

                try:
                    optional_phone=request.data.get('optional_phone')
                    ab.optional_phone=optional_phone
                    ab.save()
                    return Response({"message":'saved Successfully'},status=status.HTTP_202_ACCEPTED)
                except:
                    optional_phone=request.user.phone
                    ab.optional_phone=optional_phone
                    ab.save()
                    return Response({"message":'saved Successfully'},status=status.HTTP_202_ACCEPTED)
            except Exception as e:
                error_response = {
                    'status': 400,
                    'error': 'something_went_wrong',
                    'message': 'Something went wrong',
                    'data': {}
                }
                return Response(error_response, status=400)
        else:
            error_response = {
                        'status': 400,
                        'error': 'unsupported_user',
                        'message': 'Unsupported user',
                        'data': {}
                    }
            return Response(error_response, status=400)

    def get(self, request):

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
                
            #  Filter based on the decoded filter

            try:
                if "SWC" == request.user.user_type:
                    swc=StatePosition.objects.get(user_ref=request.user) 
                    state_level=swc.state_level     
                    data_queryset = CollectionPoint.objects.filter(waste_collector_ref__state=state_level,**decoded_filter)
                elif "WC" == request.user.user_type:
                    data_queryset = CollectionPoint.objects.filter(waste_collector_ref__user_ref=request.user)
                elif "DWC" == request.user.user_type:
                    dwc=DistrictPosition.objects.get(user_ref=request.user)
                    district_level=dwc.district_level
                    data_queryset = CollectionPoint.objects.filter(waste_collector_ref__district_level =district_level,**decoded_filter)
                else:
                    data_queryset = CollectionPoint.objects.filter(customer_ref=request.user)

            except CollectionPoint.DoesNotExist:
                error_response = {
                    'status': 404,
                    'error': 'records_not_found',
                    'message': 'No records found for the user',
                    'data': {}
                }
                return Response(error_response, status=404)

            # Serialize the queryset
            serializer = WasteCollectionPointSerializer(data=data_queryset, many=True)
            serializer.is_valid()  # Call .is_valid() before accessing .data
            serialized_data = serializer.data  # Access the serialized data

            # Print or do something with the serialized data

            return Response({"message": serialized_data})
    
        except Exception as e:
            print("Error", e)
            error_response = {
                'status': 500,
                'error': 'something_went_wrong',
                'message': 'Internal server error',
                'data': {}
            }
            return Response(error_response, status=500)
   
# Update Addresss
@permission_classes([IsAuthenticated])
class WasteCollectionPointSlugAPI(APIView):
    def put(self,request,collection_point_id):
        if "WC" == request.user.user_type:
            try:
                date=request.data.get('date')
                slot_time=request.data.get('slot_time')
                user_ref=request.user
                waste_collector_ref= get_object_or_404(WasteCollector,user_ref=user_ref)
                collection_point = get_object_or_404(CollectionPoint,collection_point_id=collection_point_id)
                collection_point.date=date
                collection_point.slot_time=slot_time
                collection_point.waste_collector_ref=waste_collector_ref
                collection_point.status="accepted"
                # print(collection_point.saved_address_ref)
                collection_point.save()
                responseData= WasteCollectionPointSerializer(collection_point,many=False).data
                return Response(responseData,status=status.HTTP_202_ACCEPTED)
            except Exception as e:
                print(e)
                error_response = {
                    'status': 400,
                    'error': 'something_went_wrong',
                    'message': 'Something went wrong',
                    'data': {}
                }
                return Response(error_response, status=400)
        else:
            error_response = {
                    'status': 400,
                    'error': 'something_went_wrong',
                    'message': 'Something went wrong',
                    'data': {}
                }
            return Response(error_response, status=400)
            


    def delete(self,request,collection_point_id):
        try:
            wp=CollectionPoint.objects.get(collection_point_id=collection_point_id)
            print(wp)
            if wp.status in ["pending","accepted"] and request.user.user_type == "USER":
                print("as",wp)
                wp.status = "cancel"
                wp.save()
                return Response({"message":"Success","id":collection_point_id},status=status.HTTP_202_ACCEPTED)

            elif wp.status == "pending" and (request.user.user_type == "WC"):
                waste_collector_ref=WasteCollector.objects.get(user_ref=request.user)
                wp.waste_collector_ref=waste_collector_ref
                wp.status = "cancel"
                wp.save()

                return Response({"message":"Success","id":collection_point_id},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            error_response = {
                'status': 400,
                'error': 'something_went_wrong',
                'message': 'Something went wrong',
                'data': {}
            }
            return Response(error_response, status=400)

    







