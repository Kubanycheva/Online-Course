from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'first_name', 'last_name', 'age',
#                   'phone_number', 'status')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#
#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError('Неверные учетные данные')
#
#     def to_representation(self, instance):
#         refresh = RefreshToken.for_user(instance)
#         return {
#             'user': {
#                 'username': instance.username,
#                 'email': instance.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'user_role', 'profile_picture', 'bio']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'course_review', 'rating', 'comment']


class CourseListSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format('%m.%Y'))
    average_rating = serializers.SerializerMethodField()
    check_good = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'created_by', 'price', 'average_rating', 'updated_at', 'check_good']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_check_good(self, obj):
        return obj.get_check_good()


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    created_by = UserProfileSimpleSerializer()

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price', 'created_by']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'category', 'description', 'created_by']


class CourseDetailUpdateDeleteAPIView(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'category', 'description', 'created_by']


class AssignmentSerializer(serializers.ModelSerializer):
    course_assignment = CourseListSerializer()
    students = UserProfileSimpleSerializer()

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course_assignment', 'students']


class LessonSerializer(serializers.ModelSerializer):
    course_lesson = CourseListSerializer()

    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content', 'course_lesson']


class ExamSerializer(serializers.ModelSerializer):
    course_exam = CourseDetailSerializer()
    duration = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Exam
        fields = ['title', 'course_exam', 'passing_score', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    student = UserProfileSimpleSerializer()
    course_certificate = CourseDetailSerializer()

    class Meta:
        model = Certificate
        fields = ['student', 'course_certificate', 'issued_at', 'certificate_url']
