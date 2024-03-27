from django.contrib import admin

from auditorium.models import Course, Lesson, Payments
from users.models import User


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'lesson', 'amount', 'field')



@admin.register(User)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff')
