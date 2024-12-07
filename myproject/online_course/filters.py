from django_filters import rest_framework as filters
from .models import Course


class CourseFilter(filters.FilterSet):
    search = filters.CharFilter(field_name='course_name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__category_name', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Course
        fields = ['search', 'category', 'min_price', 'max_price']
