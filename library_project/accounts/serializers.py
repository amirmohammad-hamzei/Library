from rest_framework import serializers
from .models import User
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        label='Phone Number',
        required=True,
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='Enter a valid 11 digit phone number starting with 09'
            ),
        ]
    )
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Username already exists'
            ),
        ])

    class Meta:
        model = User
        fields = ['phone_number', 'username', 'password']
        extra_kwargs = {'phone_number': {'required': True}}

    def create(self, validated_data):
        print(validated_data)  # for debugging purposes, remove it before production
        try:
            user = User.objects.create_user(
               phone_number=validated_data.get('phone_number'),
                username=validated_data.get('username'),
                password=validated_data.get('password')
            )
            return user
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': str(e)})


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password1', 'password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password1': 'Passwords do not match'})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Old password is incorrect'})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({'authorization': 'You are not authorized to change this password'})
        instance.set_password(validated_data['password1'])
        instance.save()
        return instance
