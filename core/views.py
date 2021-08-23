from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class ReactView(APIView):
	
	serializer_class = ReactSerializer

	def get(self, request):
		# detail = [ {"name": i.name,"detail": i.detail, "email":i.email, "dob":i.dob, "phone":i.phone}
		# for i in React.objects.all()]
		# print(detail)
		serializer = ReactSerializer(React.objects.all(), many=True)
		# print(serializer.data)
		return Response(serializer.data)

	def post(self, request):

		serializer = ReactSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			subject = 'Thank you for subscribing to our website'
			message = 'Your data has been submitted. We will get to you soon.\n\n\nBest Regards '
			email_from = settings.EMAIL_HOST_USER
			print(request.data['email'])
			recipient_list = [request.data['email']]
			print(send_mail( subject, message, email_from, recipient_list ))
			return Response(serializer.data)
		else:
			return Response(serializer.errors)
