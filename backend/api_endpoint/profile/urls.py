from django.urls import path
from .views import UpdateProfileView

urlpatterns = [
    path('', UpdateProfileView.as_view(), name='update-profile'),

]