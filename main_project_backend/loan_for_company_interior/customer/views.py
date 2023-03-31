from rest_framework.response import Response
from rest_framework import viewsets
from customer.serializers import EnquirySerializer
from customer.models import Enquiry 
from django.conf import settings
import random
from .helper import send_message



class OTPGeneration(viewsets.ViewSet):

    def create(self ,request):
        print(request.data)
        mobile = request.data.get('mobile')
        otp = random.randint(1000,9999)
        body = f"Otp for verification is {otp}"
        send_message(body=body,to=mobile)
        return Response(data={'otp':otp}, status = 200)
    
class EnquiryView(viewsets.ModelViewSet):
    serializer_class = EnquirySerializer
    queryset= Enquiry.objects.all()



       