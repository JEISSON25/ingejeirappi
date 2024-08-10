from django.shortcuts import render
from .models import Rol

from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import RolSerializer



class RolView(ListAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class CreateRolView(CreateAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

