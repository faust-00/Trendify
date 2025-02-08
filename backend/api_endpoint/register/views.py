from rest_framework.generics import CreateAPIView
from user.models import User
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            return Response({'message': "Foydalanuvchi ro'yxatdan muvaffaqiyatli o'tdi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
