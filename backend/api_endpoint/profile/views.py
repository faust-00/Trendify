from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserUpdateSerializer
from user.models import User

class UpdateProfileView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user
