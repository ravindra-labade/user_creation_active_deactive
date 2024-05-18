from uuid import uuid4
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Otp
from .serializers import UserSerializer, User


class OtpAPIView( APIView ):
    def post(self, request):
        email = request.data.get('email')
        otp = str(uuid4())
        Otp.objects.create( email=email, otp=otp)
        return Response( data={"msg": "OTP sent successfully.....!"}, status=200)


class UserAPIView( APIView ):
    def post(self, request):
        serializer = UserSerializer( data=request.data )
        if serializer.is_valid():
            username = request.data.get('username')
            otp = request.data.get('otp')
            print(otp)
            otp_obj = get_object_or_404(Otp, email=username, otp=otp)
            if otp_obj:
                serializer.save()
                return Response(data={'msg':'User Created Successfully...!!'}, status=201)
        return Response(data={'msg':'User Not Added!!!'}, status=404)

class DeactivateUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        user = User.objects.get(username=username)
        if user:
            user.is_active = False
            user.save()
            return Response({'message': 'User deactivated successfully'}, status=200)
        return Response({'error': 'User no Found'}, status=404)