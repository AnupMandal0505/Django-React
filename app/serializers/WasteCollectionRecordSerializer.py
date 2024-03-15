from rest_framework.serializers import ModelSerializer,SerializerMethodField
from app.models import WasteCollectionRecord,WasteTypeDetail
from rest_framework import serializers



class WasteCollectionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = WasteCollectionRecord
        fields = '__all__'



class WasteTypeSerializer(serializers.ModelSerializer):
    record_ref = WasteCollectionRecordSerializer()

    class Meta:
        model = WasteTypeDetail
        fields = '__all__'
