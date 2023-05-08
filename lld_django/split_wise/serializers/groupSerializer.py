from rest_framework.serializers import ModelSerializer
from ..models.group import Group

class GroupCreateSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

class GroupViewSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)