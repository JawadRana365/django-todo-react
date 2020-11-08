from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer,UserSerializer      # add this
from .models import Todo,User                     # add this

class TodoView(viewsets.ModelViewSet):       # add this
  serializer_class = TodoSerializer          # add this
  queryset = Todo.objects.all()

class UserView(viewsets.ModelViewSet):       # add this
  serializer_class = UserSerializer          # add this
  queryset = User.objects.all()

