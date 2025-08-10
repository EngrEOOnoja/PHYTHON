from unittest import TestCase
import function_snacks


class TestFunctionSnacks(TestCase):
	def test_that_function_snacks_exists(self):
		result = function_snacks.get_divide_or_square(25)
		self.assertEqual(result, 25)
		
	def test_that_get_divide_or_square_is_valid(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, -23)
	def test_that_get_divide_or_square_is_notstring(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, "sk")
	def test_that_get_divide_or_square_is_notchar(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, 'h')
	def test_that_get_divide_or_square_is_notfloat(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, float)		
				

	def test_that_function_snacks_two(self):
		self.assertEqual(function_snacks.get_only_float(56.3, 56.6), 2)
	def test_that_function_snacks_one(self):
		self.assertEqual(function_snacks.get_only_float(56, 56.6), 1)
	def test_that_function_snacks_zero(self):
		self.assertEqual(function_snacks.get_only_float(56, 5), 0)
	def test_that_function_snacks_word(self):
		self.assertRaises(ValueError, function_snacks.get_only_float, "sk", "sk")
	def test_that_function_snacks_chr(self):
		self.assertRaises(ValueError, function_snacks.get_only_float, 'h', 'h')
	


		
	def test_that_get_investment_rate_years_is_valid(self):
		self.assertEqual(function_snacks.get_investment_rate_years(5_000_000, 0.12, 60), 4_487_984_667.455309)
	def test_that_get_investment_rate_years_is_valid2(self):
		self.assertRaises(ValueError, function_snacks.get_investment_rate_years, "sk ", " yu", " yu" )
	def test_that_get_investment_rate_years_is_valid3(self):
		self.assertRaises(ValueError, function_snacks.get_investment_rate_years, 0, 0,  0 )
	def test_that_get_investment_rate_years_is_valid4(self):
		self.assertRaises(ValueError, function_snacks.get_investment_rate_years, -580, -45, -43 )
	def test_that_get_investment_rate_years_is_valid5(self):
		self.assertRaises(ValueError, function_snacks.get_investment_rate_years, 'f', 'f', 'g' )









