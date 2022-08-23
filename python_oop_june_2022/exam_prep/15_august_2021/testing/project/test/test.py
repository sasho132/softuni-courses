from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTests(TestCase):
    def test_init(self):
        name = 'Name'
        pet_shop = PetShop(name)
        self.assertEqual(pet_shop.name, name)
        self.assertListEqual([], pet_shop.pets)
        self.assertDictEqual({}, pet_shop.food)

    def test_add_food_with_quantity_equal_to_0_rise(self):
        name = 'Name'
        food_name = 'Food Name'
        pet_shop = PetShop(name)
        expected_error_message = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as error:
            pet_shop.add_food(food_name, 0)

        self.assertEqual(expected_error_message, str(error.exception))

    def test_add_food_with_not_existing_food_name(self):
        name = 'Name'
        quantity = 100
        food_name = 'Food Name'
        pet_shop = PetShop(name)

        expected_result = {food_name: quantity}
        expected_message = f"Successfully added {quantity:.2f} grams of {food_name}."
        actual_result_message = pet_shop.add_food(food_name, quantity)
        actual_result = pet_shop.food
        self.assertDictEqual(actual_result, expected_result)
        self.assertEqual(expected_message, actual_result_message)

    def test_add_food_with_existing_food_name(self):
        name = 'Name'
        quantity = 100
        food_name = 'Food Name'
        pet_shop = PetShop(name)
        pet_shop.food[food_name] = 0
        expected_result = {food_name: quantity}
        expected_message = f"Successfully added {quantity:.2f} grams of {food_name}."
        actual_result_message = pet_shop.add_food(food_name, quantity)
        actual_result = pet_shop.food
        self.assertDictEqual(actual_result, expected_result)
        self.assertEqual(expected_message, actual_result_message)

    def test_add_pet_with_not_existing_name(self):
        name = 'Name'
        pet_name = 'Pet Name'
        pet_shop = PetShop(name)
        expected_result_message = f"Successfully added {pet_name}."
        actual_result_message = pet_shop.add_pet(pet_name)
        self.assertEqual(expected_result_message, actual_result_message)
        self.assertListEqual([pet_name], pet_shop.pets)

    def test_add_pet_with_existing_name_raise(self):
        name = 'Name'
        pet_name = 'Pet Name'
        pet_shop = PetShop(name)
        pet_shop.pets.append(pet_name)
        with self.assertRaises(Exception) as error:
            pet_shop.add_pet(pet_name)
        expected_error_message = "Cannot add a pet with the same name"
        self.assertEqual(expected_error_message, str(error.exception))

    def test_feed_pet_with_not_existing_pet_raise(self):
        name = 'Name'
        pet_name = 'Pet Name'
        food_name = 'Food Name'
        quantity = 3
        pet_shop = PetShop(name)
        pet_shop.food = {food_name: quantity}
        with self.assertRaises(Exception) as error:
            pet_shop.feed_pet(food_name, pet_name)
        expected_error_message = "Please insert a valid pet name"
        self.assertEqual(expected_error_message, str(error.exception))

    def test_feed_pet_with_not_existing_food_raise(self):
        name = 'Name'
        pet_name = 'Pet Name'
        food_name = 'Food Name'
        pet_shop = PetShop(name)
        pet_shop.pets.append(pet_name)
        actual_result_message = pet_shop.feed_pet(food_name, pet_name)
        expected_error_message = f'You do not have {food_name}'
        self.assertEqual(expected_error_message, actual_result_message)

    def test_feed_pet_with_food_quantity_bellow_100(self):
        name = 'Name'
        pet_name = 'Pet Name'
        food_name = 'Food Name'
        quantity = 3
        pet_shop = PetShop(name)
        pet_shop.add_pet(pet_name)
        pet_shop.add_food(food_name, quantity)
        actual_result = pet_shop.feed_pet(food_name, pet_name)
        expected_food_quantity = 1003.00
        expected_result = "Adding food..."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_food_quantity, pet_shop.food[food_name])

    def test_feed_with_food_quantity_over_100(self):
        name = 'Name'
        pet_name = 'Pet Name'
        food_name = 'Food Name'
        quantity = 103
        pet_shop = PetShop(name)
        pet_shop.add_pet(pet_name)
        pet_shop.add_food(food_name, quantity)
        actual_result = pet_shop.feed_pet(food_name, pet_name)
        expected_food_quantity = 3
        expected_result = f"{pet_name} was successfully fed"
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_food_quantity, pet_shop.food[food_name])

    def test_repr(self):
        name = 'Name'
        pet_name = 'Pet Name'
        food_name = 'Food Name'
        quantity = 103
        pet_shop = PetShop(name)
        pet_shop.add_pet(pet_name)
        pet_shop.add_food(food_name, quantity)
        expected_message = f'Shop {pet_shop.name}:\nPets: {", ".join(pet_shop.pets)}'
        actual_message = repr(pet_shop)
        self.assertEqual(expected_message, actual_message)


if __name__ == '__main__':
    main()
