from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User   # ✅ fixed
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        if not data.get('activity_type'):
            raise serializers.ValidationError({"activity_type": "Activity type is required."})

        if not data.get('duration_minutes') or data['duration_minutes'] <= 0:
            raise serializers.ValidationError({"duration_minutes": "Duration must be greater than 0."})

        if not data.get('date'):
            raise serializers.ValidationError({"date": "Date is required."})

        if 'distance' in data and data['distance'] is not None and data['distance'] < 0:
            raise serializers.ValidationError({"distance": "Distance cannot be negative."})

        if 'calories' in data and data['calories'] is not None and data['calories'] < 0:
            raise serializers.ValidationError({"calories": "Calories cannot be negative."})

        return data


class ActivityMetricsSerializer(serializers.Serializer):
    total_duration = serializers.FloatField()
    total_distance = serializers.FloatField()
    total_calories = serializers.FloatField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
