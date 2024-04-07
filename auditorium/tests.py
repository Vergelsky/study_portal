from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from auditorium.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='testuser@mail.com')
        self.course = Course.objects.create(name='testcourse', description='testcoursedescription')
        self.lesson = Lesson.objects.create(name='testlesson1', description='testlessondescription1',
                                            course=self.course, owner=self.user)
        self.data = {
            'name': "testlesson2",
            'description': 'testlessondescription2',
            'course': self.course.pk
        }

    def test_create_lesson(self):
        """Тестируем создание урока"""

        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('auditorium:lesson-create'), data=self.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_read_lesson(self):
        """ Тестируем чтение урока """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('auditorium:lesson-list'), data=self.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """ Тестируем обновление урока """

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('auditorium:lesson-update', args=[self.lesson.pk]),
                                     data={'name': 'newtest', 'description': 'newdescription'})
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """ Тестируем обновление урока """

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('auditorium:lesson-delete', args=[self.lesson.pk]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='testuser@mail.com')
        self.course = Course.objects.create(name='testcourse', description='testcoursedescription')


    def subscribe(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('auditorium:subscribe')
        return self.client.post(url, data={'course': self.course.id}).status_code

    def test_subscribe(self):
        """ Тестируем подписку"""
        self.assertEqual(
            self.subscribe(),
            status.HTTP_200_OK
        )

    def test_unsubscribe(self):
        """ Тестируем отписку"""
        self.assertEqual(
            self.subscribe(),
            status.HTTP_200_OK
        )