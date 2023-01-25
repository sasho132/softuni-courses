from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTesting(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('TestName', 10)

    def test_init(self):
        valid_ingredients = ["white", "yellow", "blue", "green", "red"]

        self.assertEqual(self.paint_factory.name, 'TestName')
        self.assertEqual(self.paint_factory.capacity, 10)
        self.assertDictEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, valid_ingredients)

    def test_add_not_valid_ingredient_expect_raise(self):
        ingredient = 'not_valid_ingredient'
        expected_result = f"Ingredient of type {ingredient} not allowed in PaintFactory"

        self.assertDictEqual(self.paint_factory.ingredients, {})
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient(ingredient, 1)
        self.assertDictEqual(self.paint_factory.ingredients, {})

        self.assertEqual(expected_result, str(error.exception))

    def test_add_ingredient_with_not_valid_quantity_expect_raise(self):
        product_type = 'white'
        product_quantity = 10
        expected_result = "Not enough space in factory"

        self.assertDictEqual(self.paint_factory.ingredients, {})
        self.paint_factory.add_ingredient(product_type, 1)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual(expected_result, str(error.exception))
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 1})

    def test_add_ingredient_expected_to_be_added(self):
        product_type = 'white'
        product_quantity = 3

        self.assertDictEqual(self.paint_factory.ingredients, {})
        self.paint_factory.add_ingredient(product_type, product_quantity)
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 3})

        self.paint_factory.add_ingredient('white', 2)
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 5})

    def test_remove_not_valid_ingredient_expect_to_raise(self):
        product_type = 'brown'
        product_quantity = 3
        expected_result = "'No such ingredient in the factory'"

        self.paint_factory.add_ingredient('white', 3)
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 3})
        self.assertEqual(expected_result, str(error.exception))

    def test_remove_ingredient_with_not_valid_quantity_raise(self):
        product_type = 'white'
        product_quantity = 5
        expected_result = "Ingredients quantity cannot be less than zero"

        self.paint_factory.add_ingredient('white', 3)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 3})
        self.assertEqual(expected_result, str(error.exception))

    def test_remove_ingredient_with_valid_quantity_expect_to_be_removed(self):
        product_type = 'white'
        product_quantity = 3

        self.paint_factory.add_ingredient(product_type, 8)
        self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertDictEqual(self.paint_factory.ingredients, {'white': 5})

    def test_products_property(self):
        expected_result = {'white': 3}
        self.paint_factory.add_ingredient('white', 3)
        self.assertDictEqual(expected_result, self.paint_factory.products)

    def test_repr(self):
        self.paint_factory.add_ingredient('white', 3)
        self.paint_factory.add_ingredient('green', 1)

        expected_result = f"Factory name: TestName with capacity 10.\n" \
                          f"white: 3\ngreen: 1\n"

        self.assertEqual(expected_result, self.paint_factory.__repr__())


if __name__ == "__main__":
    main()
