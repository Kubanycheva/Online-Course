from .models import Course, Category
from modeltranslation.translator import TranslationOptions,register


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)
