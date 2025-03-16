from rest_framework import serializers
from django.contrib.auth.models import User

from restaurant_review.models import SillaProject, SillaUser, LANGUAGE_CHOICES, STYLE_CHOICES



class UserSerializer(serializers.ModelSerializer):
    sillausers = serializers.PrimaryKeyRelatedField(many=True, queryset=SillaUser.objects.all())
    sillaprojects = serializers.PrimaryKeyRelatedField(many=True, queryset=SillaProject.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'sillausers','sillaprojects']



class SillaProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SillaProject
        fields = ['id', 'name', 'owner',  'description', 'location', 'total_material_cost_price', 'total_labor_cost_price', 'total_other_cost_price']


class SillaUserSerializer(serializers.ModelSerializer):    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SillaUser
        fields = ['id', 'name', 'email', 'phone', 'birthday', 'owner']



