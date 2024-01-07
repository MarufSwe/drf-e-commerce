from django.test import TestCase

from e_products.models import Product
from e_products.serializers.product_serializer import ProductSerializer


class ProductSerializerTestCase(TestCase):
    def test_product_serializer(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '10.00',
            'stock_status': 5
        }
        product = Product.objects.create(**product_data)
        serializer = ProductSerializer(product)
        expected_data = {
            'id': product.id,
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '10.00',
            'image': None,
            'stock_status': 5,
            'reviews': []
        }
        self.assertEqual(serializer.data, expected_data)
