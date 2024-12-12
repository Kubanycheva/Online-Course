from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=400)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель'),
        ('администратор', 'администратор'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='клиент')
    profile_picture = models.ImageField(upload_to='profile')
    bio = models.TextField()


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, default='начальный')
    price = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def get_average_rating(self):
        ratings = self.review.all()
        if ratings.exists():
            return round(sum(rating.rating for rating in ratings) / ratings.count(), 1)
        return 0

    def get_check_good(self):
        ratings = self.review.all()
        if ratings.exists():
            num = 0
            for i in ratings:
                if i.rating > 3:
                    num += 1
            return f'{(num * 100) / ratings.count()}%'

        return f'0%'


class Lesson(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)
    video_url = models.FileField(upload_to='vid/', verbose_name='Видео', null=True, blank=True)
    content = models.TextField()
    course_lesson = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()
    due_date = models.DateField(auto_now_add=True)
    course_assignment = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='assignment')
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='students')

    def __str__(self):
        return f'{self.title} - {self.due_date}'


class Exam(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)
    course_exam = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='exam')
    passing_score = models.IntegerField(default=0)
    duration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course_exam} - {self.title}'


class ExamQuestions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_questions')
    questions = models.CharField(max_length=65, null=True, blank=True)


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='student')
    course_certificate = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='certificate')
    issued_at = models.DateField(auto_now=True)
    certificate_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.issued_at} - {self.certificate_url}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_review = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.rating}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f'{self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.course} - {self.quantity}'


class Favorite(models.Model):
    user = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_date}'


class FavoriteLesson(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson} - {self.cart}'



