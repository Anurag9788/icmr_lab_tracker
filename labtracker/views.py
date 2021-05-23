from django.shortcuts import render
from django.http import HttpResponse
from .models import Lab
from django.http import JsonResponse
from django.contrib import messages
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import requests
from urllib import parse
from trackerapp.settings import Mapbox_token
import json
from trackerapp.settings import BASE_DIR
import socket
import geoip2.database



# Create your views here.
def index(request):
    lab_list=Lab.objects.order_by("name")
    print(BASE_DIR)
    context={ 'lab_list': lab_list}
    return render(request,'labtracker/index.html',context)

def serach_view(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET': # If the form is submitted
        
        search_query = request.GET.get('search_box', None)

        lab_list=Lab.objects.order_by("name")
        print(lab_list)
        context={ 'lab_list': lab_list}

        if search_query is not None:
            records=Lab.objects.filter(name__icontains=search_query).first()
            records_list =Lab.objects.filter(name__icontains=search_query)
            
            search_text="icmr+delhi"
            if records is not None:
                search_text = parse.quote(records.address)

            url= "https://api.mapbox.com/geocoding/v5/mapbox.places/{search_text}.json?access_token={mapbox_token}"
            url = url.format(
            search_text=search_text,
            mapbox_token = Mapbox_token
            )

            data= json.loads(requests.get(url).content.decode('utf-8'))
            data = data['features']
        
            context['co-ordinate']= data[0]['center']
            context['query']    = search_text
            context['records'] = records
            context['records_list'] = records_list
        else:
            data = " "
        
            context={}

    return render(request,'labtracker/index.html',context)   
def searc_lab_list(request):
    if request.method == 'GET': # If the form is submitted

        
        search_query = request.GET.get('search_box', None)
        print(search_query)

        
        context={}
        if search_query is not None:
            print("below recors list")
            records_list =Lab.objects.filter(address__icontains=str(search_query))
            print(records_list)
            context['records_list'] = records_list
        else:
            context['records_list'] = " "
            print(records_list)

    return render(request,'labtracker/second.html',context)   

def search_near_lab (request):
    if request.method == 'GET': # If the form is submitted
        context={}

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
        try:
            socket.inet_aton(ip)
            ip_valid = True
        except socket.error:
            ip_valid = False
        if ip_valid:
            reader = geoip2.database.Reader('./GeoLite2-City_20210518/GeoLite2-City.mmdb')
            try:
                url1 ="https://ipgeolocation.abstractapi.com/v1/?api_key={key}&ip_address={ip}"
                url1 = url1.format(
                key='cfd4c58a01a340959a39aad7e3275e4d',
                ip = ip
                )

                data_lo= (requests.get(url1))
                data_lo = json.loads(data_lo.text)['city']
                response = data_lo
                


                
            except:
                response = reader.city(ip)
                print(response.country.iso_code)
                print(response.country.name)
                print(response.subdivisions.most_specific.name)
                print(response.subdivisions.most_specific.iso_code)
                print(response.city.name)
                print(response.postal.code)
                print(response.location.latitude)
                print(response.location.longitude)
                response = response.city.name
            record = Lab.objects.filter(address__icontains=(response)).first()
            context['record'] = record
        else:
            context['record'] = " "

    return render(request,'labtracker/second.html',context)  


    