from rest_framework.serializers import ModelSerializer
from app.models import User, WasteCollector,DistrictPosition,StatePosition
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'delete']


class UserWasteCollectorSerializer(ModelSerializer):
    user_ref = UserSerializer()
    class Meta:
        model = WasteCollector
        fields = '__all__'

class UserDistrictCollectorSerializer(ModelSerializer):
    user_ref = UserSerializer()
    class Meta:
        model = DistrictPosition
        fields = '__all__'



class UserStateCollectorSerializer(ModelSerializer):
    user_ref = UserSerializer()
    class Meta:
        model = StatePosition
        fields = '__all__'


