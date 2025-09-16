from rest_framework import viewsets, generics
from .models import (Skill, UserProfile, SocialNetwork, Category, Project, Offer, Review)
from .serializers import (SkillSerializer, UserProfileSerializer, SocialNetworkSerializer, CategoryListSerializer,
                          ProjectListSerializer,ProjectDetailSerializer, OfferSerializer, CategoryDetailSerializer,
                          ReviewSerializer)



class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer



class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer



class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




