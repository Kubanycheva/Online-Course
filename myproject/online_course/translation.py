from .models import (Category, Course, Lesson, Assignment, Exam, Review,
                     Certificate, ExamQuestions, UserProfile)
from modeltranslation.translator import TranslationOptions, register


@register(UserProfile)
class UserprofileTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(ExamQuestions)
class ExamTranslationOptions(TranslationOptions):
    fields = ('questions', )


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('certificate_url',)
