from .models import Project
from django_filters import FilterSet


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'category': ['exact'],
            'budget': ['gt', 'lt']
        }