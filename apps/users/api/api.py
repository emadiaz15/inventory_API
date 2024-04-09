from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    
    if request.method == 'GET': #list
        users =User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    elif request.method == 'POST': #create
        users_serializer = UserSerializer(data = request.data)
        
        if users_serializer.is_valid(): #validacion
            users_serializer.save()
            return Response({'menssage':'user create successfully'},status = status.HTTP_201_CREATED)
        return Response(users_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk = None):
    
    user = User.objects.filter(id = pk).first() #queryset
    
    if user: #valiadacion
        
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user,data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response({'menssage':'user deleted successfully'},status = status.HTTP_200_OK)
    
    return Response({'menssage':'User not found'},status = status.HTTP_400_BAD_REQUEST)