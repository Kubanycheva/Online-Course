from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')
router.register(r'category', CategoryViewSet, basename='category-list')
router.register(r'course', CourseListViewSet, basename='course-list')
router.register(r'course-detail', CourseDetailViewSet, basename='course-detail')
router.register(r'lesson', LessonViewSet, basename='lesson-list')
router.register(r'assignment', AssignmentViewSet, basename='assignment-list')
router.register(r'exam', ExamViewSet, basename='exam-list')
router.register(r'certificate', CertificateViewSet, basename='certificate-list')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'review-detail', ReviewViewSet, basename='review-detail')


urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
=======

>>>>>>> 4645b488c2ca1377e19f3fb4e8d8a4f1bbbdbf1f
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
