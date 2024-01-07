from django.test import TestCase

from e_products.models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            price='10.00',
            stock_status=5
        )

    def test_product_str_representation(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(str(product), 'Test Product')
