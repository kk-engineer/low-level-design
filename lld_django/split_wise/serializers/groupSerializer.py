from rest_framework.serializers import ModelSerializer
from ..models.group import Group
from .userSerializer import UserViewSerializer

class GroupCreateSerializer(ModelSerializer):
    #participants = UserViewSerializer()

    class Meta:
        model = Group
        fields = '__all__'

class GroupViewSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)