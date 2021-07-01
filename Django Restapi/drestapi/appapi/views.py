from django.shortcuts import render
from rest_framework.decorators import api_view
from appapi.serializers import UserSerializer, PersonSerializer
from rest_framework.response import Response
from appapi.models import User, Person
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def signup(request): 
	if request.method == 'POST':
		try:
			users = User.objects.get(email = request.data['email'])
			if request.data['email'] == users.email:			
				return Response({"data":"registered"})
		except:
			user_serializer = UserSerializer(data = request.data)
			if user_serializer.is_valid():
				password = make_password(request.data['password'])
				user_serializer.save(password=password)
				return Response("HTTP_201_CREATED") 
			return Response("HTTP_400_BAD_REQUEST")

@api_view(['POST'])
def login(request): 
	if request.method == 'POST':
		try:
			users = User.objects.get(email = request.data['email'])
			if request.data['email'] == users.email:
				if check_password(request.data['password'], users.password):
					return Response({"message":"success", "username":users.username})
				else:
					return Response({"message":"password wrong"})
			else:
				return Response({"message":"wrong email"})
		except:
			return Response({"message":"no credential found"})

@api_view(['GET'])		
def show(request,email):
	if request.method == 'GET':		
		try:
			users = Person.objects.filter(userid=email)
			person_serializer = PersonSerializer(users, many=True)
			return Response(person_serializer.data)
		except:
			return Response({"message":"no data found"})

@api_view(['GET'])		
def show_id(request,id):
	if request.method == 'GET':		
		try:
			users = Person.objects.get(id=id)
			person_serializer = PersonSerializer(users, many=False)
			return Response(person_serializer.data)
		except:
			return Response({"message":"no data found"})

@api_view(['POST'])
def createperson(request): 
	if request.method == 'POST':
		person_serializer = PersonSerializer(data = request.data)
		if person_serializer.is_valid():
			person_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")

@api_view(['POST'])
def updateperson(request, id):
	users = Person.objects.get(id=id)
	if request.method == 'POST':
		person_serializer = PersonSerializer(users, data = request.data, many=False, partial=True)
		if person_serializer.is_valid():
			person_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")

@api_view(['DELETE'])
def deleteperson(request, id):
	users = Person.objects.get(id=id)
	users.delete()
	return Response("Delete succes")



    
