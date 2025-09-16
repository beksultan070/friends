from .models import (Skill, UserProfile, SocialNetwork,Category,
                     Project, Offer, Review)
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']


class SocialNetworkSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = SocialNetwork
        fields = ['id', 'users', 'name', 'url']



class OfferSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Offer
        fields = ['message', 'proposed_budget', 'proposed_deadline', 'created_date']




class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'budget', 'description']


class ReviewSerializer(serializers.ModelSerializer):
    reviews_written = UserProfileRoleSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['reviews_written','rating','comment','created_at']




class ProjectDetailSerializer(serializers.ModelSerializer):
     offers = OfferSerializer(many=True, read_only=True)
     clients = UserProfileRoleSerializer(many=True, read_only=True)
     comments = ReviewSerializer(many=True, read_only=True)
     skills_required = SkillSerializer(many=True)
     created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

     class Meta:
        model = Project
        fields = ['title', 'budget', 'description', 'deadline', 'status',
                  'skills_required', 'created_at', 'offers', 'clients', 'comments']




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']



class CategoryDetailSerializer(serializers.ModelSerializer):
    projects = ProjectListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'projects']

