from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from ..models.user import User
from ..models.userProfile import UserProfile

class UserCreateSerializer(ModelSerializer):
    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        user = User.objects.create(**validate_data)
        UserProfile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )

class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', )