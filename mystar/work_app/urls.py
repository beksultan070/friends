from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.routers import DefaultRouter
from .views import (SkillViewSet, UserProfileViewSet, SocialNetworkViewSet,
                    CategoryListAPIView,CategoryDetailAPIView,
                    ProjectListAPIView,ProjectDetailAPIView,
                    OfferViewSet, ReviewViewSet)
from django.urls import path, include

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'social_networks', SocialNetworkViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/', ProjectListAPIView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail')
]