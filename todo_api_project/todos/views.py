from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import *

# Create your views here.

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return TodoUpdateSerializer
        return TodoDefaultSerializer

    def create(self, request):
        new_data = request.data.copy()
        new_data['created_by']=request.user.pk
        serializer = TodoDefaultSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
