from .serializers import ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reviews
from django.contrib.auth.models import User
from django.db.models import Q
from . import util
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Review(APIView):

    #Upload Image.

    def post(self, request, *args, **kwargs):
        try:
            data = request.data  
            title = len(data['title'])
            description = len(data['description'])

            if(util.verification(title,description) == False):
                return Response(status=status.HTTP_403_FORBIDDEN)

            serial = ReviewSerializer(data=request.data)

            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    #Upgrade Image.

    def put(self, request, *args, **kwargs):

        try:

            data = request.data
            id = self.kwargs['id']
            title = len(data['title'])
            description = len(data['description'])
            token = request.data['token']
                    
            infoWithImg = {'title': data['title'], 'description': data['description'], 'img': data['img'],'user': data['user']}
            
            if(util.verification(title,description) == False):
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            list = Reviews.objects.get(id=id)

            serial = ReviewSerializer(list,data=infoWithImg)

            if serial.is_valid():

                UserId = ReviewSerializer(list).data

                userList = User.objects.filter(first_name=token,id=UserId['user'])

                if(len(userList) == 0):
                     return Response(status=status.HTTP_403_FORBIDDEN)
                else:
                    serial.save()
                    
                    util.deleteImg(UserId['img'])
                    
                    return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        

    #Delete Image.

    def delete(self, request, *args, **kwargs):
        try:

            token = request.data['token']
            id = self.kwargs['id']

            list = Reviews.objects.filter(id=id)

            if(len(list) == 0):
                return Response(status=status.HTTP_403_FORBIDDEN)

            serial = ReviewSerializer(list,many=True)

            userList = User.objects.filter(first_name=token,id=serial.data[0]['user'])
            

            if(len(userList) == 0):
                return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                list.delete()
                util.deleteImg(serial.data[0]['img'])
                return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    #Get single review.    
        
    def get(self, *args, **kwargs):
        try:
            id = self.kwargs['id']
            list = Reviews.objects.filter(id=id)

            serial = ReviewSerializer(list,many=True)

            if(len(serial.data) == 0):
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(serial.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#Get all reviews.

class AllReviews(APIView):
            permission_classes = [IsAuthenticated]
            def get(self, request, *args, **kwargs):
                              
                try: 
                     list = Reviews.objects.all()
                     serial = ReviewSerializer(list,many=True)
                     return Response(serial.data)
                except:
                  return Response(status=status.HTTP_400_BAD_REQUEST)

#Get user reviews.

class UserReviews(APIView):
            permission_classes = [IsAuthenticated]
            def get(self, request, *args, **kwargs):
                try: 
                     user = self.kwargs['user']
                     id = self.kwargs['id']

                     list = Reviews.objects.filter(Q(user = id) & ~Q(id = user))

                     if (len(list) == 0):
                         return Response(status=status.HTTP_204_NO_CONTENT)   
                     else:
                        serial = ReviewSerializer(list,many=True)
                        return Response(serial.data)
                except:
                  return Response(status=status.HTTP_400_BAD_REQUEST)

class test(APIView):
            def get(self, request, *args, **kwargs):
                try: 
                    Response({"ddd":"esta"})
                except:
                  return Response(status=status.HTTP_400_BAD_REQUEST)

          

