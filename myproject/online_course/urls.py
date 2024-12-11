from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')
router.register(r'category', CategoryViewSet, basename='category-list')
router.register(r'lesson', LessonViewSet, basename='lesson-list')
router.register(r'assignment', AssignmentViewSet, basename='assignment-list')
router.register(r'exam', ExamViewSet, basename='exam-list')
router.register(r'certificate', CertificateViewSet, basename='certificate-list')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'review-detail', ReviewViewSet, basename='review-detail')


urlpatterns = [
    path('', include(router.urls)),

    #
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('create_course/', CourseCreateAPIView.as_view(), name='course_create'),
    path('create_course/<int:pk>', CourseDetailUpdateDeleteAPIView.as_view(), name='course_create'),

]
