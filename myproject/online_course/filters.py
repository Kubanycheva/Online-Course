<<<<<<< HEAD
=======
import django_filters
from django_filters.rest_framework import FilterSet
from .models import *


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'level': ['exact'],
            'price': ['exact']

        }

>>>>>>> 5d48fff8455dfe79c07639de137faf8ed162cb4c
