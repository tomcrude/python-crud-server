from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializer
from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
from . import util
from random import randrange
#from rest_framework.authtoken.models import Token


@api_view(['POST'])
def CreateUser(request):
        if (request.method == 'POST'):
                try:
                    data = request.data
                    username =  data['username']  
                    password =  data['password']
                    email =  data['email'] 
                    token = username + "-" + str(randrange(100000))

                    veri = util.Verification(username,password,email)
 
                    if(veri != None):
                          return Response(veri) 
    
                    User.objects.create(
                            username = username,
                            email = email,
                            password = make_password(password),
                            first_name = token
                        )
                    return Response(status = status.HTTP_201_CREATED)
                
                except IntegrityError:
                    return Response(status = status.HTTP_403_FORBIDDEN)

                except:
                    return Response(status = status.HTTP_400_BAD_REQUEST)   
                
        else:
                Response(status = status.HTTP_404_NOT_FOUND)
                

@api_view(['POST'])
def LogIn(request):
        if (request.method == 'POST'):

            try:
                 data = request.data
                 username =  data['username']  
                 password =  data['password']

                 list = User.objects.filter(username=username)

                 #list2 = User.objects.get(username=username)

                 if (len(list) == 0):
                      return Response(status = status.HTTP_403_FORBIDDEN)
                 
                 serial = serializer.UserSerial(list, many=True)    
                 
                 if (check_password(password,serial.data[0]['password']) == False):
                       return Response(status = status.HTTP_403_FORBIDDEN)
                 
                 #token = Token.objects.get_or_create(user=list2)
                  
                 return Response(serial.data)   
                           
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)         
               
        else:
                Response(status = status.HTTP_404_NOT_FOUND)


      

