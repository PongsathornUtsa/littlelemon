from django.db import models
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date.strftime('%Y-%m-%d %H:%M')}"

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=200, inventory=50)
        Menu.objects.create(title="Burger", price=100, inventory=50)

    def test_get_all(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)