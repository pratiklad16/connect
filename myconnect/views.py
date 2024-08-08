from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import myconnect
from connect.serializers import MyConnectSerializer

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

        if cities:
            print("Hello world Cities")
            myconnects = myconnects.filter(city__in=[city.strip().lower() for city in cities])
        
        if domains:
            print("Hello world Domains")
            myconnects = myconnects.filter(domain__in=[domain.strip().lower() for domain in domains])
        
        if interests:
            print("Hello world interests")
            myconnects = myconnects.filter(interest__in=[interest.strip().lower() for interest in interests])
        
        if level:
            print("Hello world level")
            myconnects = myconnects.filter(levels=level)

        serializer = MyConnectSerializer(myconnects, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    else:
        # Handle GET request
        return render(request, 'filter.html')
