from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from auditorium.models import Course, Lesson, Payments, Subscribe
from auditorium.pagination import PageNumberPagination
from auditorium.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscribeSerializer
from users.permissions import IsModerator, IsOwner


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = PageNumberPagination


    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ('list', 'retrieve'):
            self.permission_classes = [IsAuthenticated]
        elif self.action in ('update', 'partial_update'):
            self.permission_classes = [IsOwner or IsModerator]
        elif self.action in ('destroy',):
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = PageNumberPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner or IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner or IsAdminUser]


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'field')
    ordering_fields = ('date',)


class SubscribeAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscribe.objects.filter(user=user, course=course_id)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscribe.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'

        return Response({'message': message})
