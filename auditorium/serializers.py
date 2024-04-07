from rest_framework import serializers

from auditorium.models import Lesson, Course, Payments, Subscribe
from auditorium.validators import CorrectLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [CorrectLinkValidator(fields=['video', 'description'])]


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()
    is_user_subscribed = serializers.SerializerMethodField()
    lesson_set = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [CorrectLinkValidator(fields=['description'])]

    def get_lessons_qty(self, instance):
        return instance.lesson_set.all().count()

    def get_is_user_subscribed(self, instance):
        user = self.context.get('request').user
        return instance.subscribe_set.filter(user=user).exists()

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


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        feilds = '__all__'
