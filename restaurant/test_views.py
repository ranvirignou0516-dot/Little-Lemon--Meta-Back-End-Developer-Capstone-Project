from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from restaurant.models import Menu


class MenuViewTest(APITestCase):

    def test_menu_list(self):
        Menu.objects.create(
            title="Pizza",
            price=250,
            inventory=10
        )

        response = self.client.get("/restaurant/menu/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Pizza")