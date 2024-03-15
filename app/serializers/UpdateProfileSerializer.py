from rest_framework import serializers
from app.models import User


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user_id', 'phone','email','password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set required=False for all fields except excluded ones
        for field_name, field in self.fields.items():
            if field_name not in self.Meta.exclude:
                field.required = False