from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title='Pizza', price=9.99, inventory=100)
        Menu.objects.create(title='Burger', price=5.99, inventory=100)
        Menu.objects.create(title='Pasta', price=7.49, inventory=100)
    
    def test_getall(self):
        all_menus = Menu.objects.all()
        self.assertEqual(all_menus.count(), 3)

        # Serialize the data
        serializer = MenuSerializer(all_menus, many=True)
        serialized_data = serializer.data

        # Convert expected data to match the serialized format (price as string)
        expected_data = [
            {
                'id': menu.id,
                'title': menu.title,
                'price': str(menu.price),  # Convert price to string
                'inventory': menu.inventory
            }
            for menu in all_menus
        ]

        # Assert that the serialized data matches the expected data
        self.assertEqual(serialized_data, expected_data)
