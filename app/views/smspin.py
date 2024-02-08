from django.views import View
from app.models import User,WasteCollector,CollectionPoint
import random

from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from app.serializers.userSerializer import UserSerializer

from django.core.mail import send_mail,EmailMultiAlternatives
# from django.contrib import messages
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView

from django.template.loader import render_to_string

  

@permission_classes([IsAuthenticated]) 
class SmsPinAPI(APIView):
    def post(self, request):
        try:
            data=request.data
            collection_point_id=data['collection_point_id']
            cp=CollectionPoint.objects.get(collection_point_id=collection_point_id)
            user_email=cp.customer_ref.email

            # Example list of items
            items = [
                {'waste_type': 'Plastic', 'quantity': 2, 'unit': 'kg', 'total_price': 30.0},
                {'waste_type': 'Paper', 'quantity': 3, 'unit': 'kg', 'total_price': 45.0},
                # Add more items as needed
            ]            
            
            
            # Calculate total price
            total_price = sum(item['total_price'] for item in items)

            mail(items,total_price,user_email)
            return Response({"message":'Pin Send'},status=status.HTTP_201_CREATED)     

        except Exception as e:
            print(e)
            error_response = {
                'status': 400,
                'error': 'something_went_wrong',
                'message': 'SMS Failed',
                'data': {}
            }
            
            return Response({"message":error_response},status=status.HTTP_400_BAD_REQUEST)     





def mail(items,total_price,email):
    subject = 'PIN COMFORMATION'
    from_email = 'mastikipathshala828109@gmail.com'

     # Correct template_path and render the HTML template with the provided data
    template_path = 'emailtem.html'
    pin=random.randint(99999,99999999)
    context = {'pin': pin,
               'items':items,
               'total_price':total_price,
               }
    message = render_to_string(template_path, context)

    to = email

    try:
        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        msg.send()
        # return Response({"message":'Mails Send'},status=status.HTTP_400_BAD_REQUEST)     
    except Exception as e:
            print(e)
            # error_response = {
            #     'status': 400,
            #     'error': 'something_went_wrong',
            #     'message': 'Something went wrong',
            #     'data': {}
            # }
            # return Response(error_response, status=400)
            raise Exception("Prob")

