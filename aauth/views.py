from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_auth.app_settings import LoginSerializer, UserDetailsSerializer

class LoginView(GenericAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    
    def login(self):
        self.user = self.serializer.validated_data['user']

    def get_response_serializer(self):
        return UserDetailsSerializer

    def get_response(self):
        serializer_class = self.get_response_serializer()

        data = self.user.__dict__

        serializer = serializer_class(instance=data, context={'request': self.request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        
        self.login()
        return self.get_response()