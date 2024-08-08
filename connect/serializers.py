from rest_framework import serializers

from myconnect.models import myconnect
class MyConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = myconnect
        fields = '__all__'
        