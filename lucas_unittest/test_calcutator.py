import unittest
from unit_test import Calculator
class TestCalculator(unittest.TestCase):
    # raise keyword
    # arrange
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_add_two_positive_numbers(self):
        # arrange
        # calculator = Calculator()
        
        # act
        # assert
        self.assertEqual( self.calculator.add(3,4),7 )

    def test_add_number_to_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.add('a',4)
        # with assertionError want failure not error
        # assetRaisers(TypeError)

    