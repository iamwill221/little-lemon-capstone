from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item = Menu.objects.create(title="Pizza", price=70, inventory=100)
        item = Menu.objects.create(title="Burger", price=1200, inventory=100)

    def test_getall(self):
        client = Client()
        response = client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)