from django.shortcuts import render
from .models import Blood
from .serializers import BloodSerializer
from rest_framework.response import Response
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class BloodView(ListCreateAPIView):
	queryset = Blood.objects
	serializer_class = BloodSerializer

	def perform_create(self, serializer):
		return serializer.save()
		# data = self.request.data
		# blood = Blood(
		# 	name=data.get('name'),
		# 	year=data.get('year'),
		# 	email=data.get('email'),
		# 	blood_group=data.get('blood_group'),
		# 	corona_status=data.get('corona_status'),
		# 	last_checked_date=data.get('last_checked_date'),
		# )
		# return serializer.save()

class SingleBloodView(RetrieveUpdateDestroyAPIView):
	queryset = Blood.objects
	serializer_class = BloodSerializer
