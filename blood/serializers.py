from rest_framework import serializers
from .models import Blood

class BloodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blood
		fields = ('id', 'name', 'year', 'email', 'blood_group', 'corona_status', 'last_checked_date')
