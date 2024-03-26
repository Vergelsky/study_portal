from rest_framework import serializers

from auditorium.models import Lesson, Course


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_qty(self, instance):
        return instance.lesson_set.all().count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
