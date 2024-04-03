from rest_framework import serializers

from auditorium.models import Lesson, Course, Payments
from auditorium.validators import CorrectLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [CorrectLinkValidator(fields=['video', 'description'])]


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()
    lesson_set = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [CorrectLinkValidator(fields=['description'])]

    def get_lessons_qty(self, instance):
        return instance.lesson_set.all().count()

    def create(self, validated_data):
        lessons = validated_data.pop('lesson_set')

        course_item = Course.objects.create(**validated_data)

        for l in lessons:
            Lesson.objects.create(**l, course=course_item)

        return course_item


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
