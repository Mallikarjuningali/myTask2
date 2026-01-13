from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import HelloWorld

class HelloWorldTests(APITestCase):
    def test_create_and_retrieve_hello_world(self):
        """
        Ensure we can create a new hello world message and retrieve it.
        """
        url = reverse('helloworld-list')
        data = {'message': 'Hello, Test!'}
        
        # Test Create
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HelloWorld.objects.count(), 1)
        self.assertEqual(HelloWorld.objects.get().message, 'Hello, Test!')

        # Test List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], 'Hello, Test!')
