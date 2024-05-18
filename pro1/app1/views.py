from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Employee, EmployeeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, \
    IsAdminUser





class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
