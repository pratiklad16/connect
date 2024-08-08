from django.shortcuts import render
from connect.serializers import MyConnectSerializer
from rest_framework.decorators import api_view
from .models import myconnect
from django.http import HttpResponse, JsonResponse
# Create your views here.
@api_view(['GET'])
def home(request):
    myconnects = myconnect.objects.all()
    serializer = MyConnectSerializer(myconnects, many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST', 'GET'])
def filter(request):
    if request.method == 'POST':
        level = request.data.get('level')
        cities = request.data.getlist('city[]')
        domains = request.data.getlist('domain[]')
        interests = request.data.getlist('interest[]')
        print(level)
        print(cities)
        print(domains)
        print(interests)
    myconnects = myconnect.objects.all()
    serializer = MyConnectSerializer(myconnects, many=True)
    
    return render(request, 'filter.html', {'serializer': serializer})