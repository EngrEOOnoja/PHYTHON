from unittest import TestCase
import code_leveling

class TestFunctionTask(TestCase):
	def test_that_code_leveling_exist(self):
		code_leveling.to_add_tuple
	def test_that_code_leveling_is_valid(self):
		self.assertRaises(ValueError, code_leveling.to_add_tuple, "y", "t" )	
	def test_that_code_leveling_is_valid1(self):
		self.assertRaises(ValueError, code_leveling.to_add_tuple, "come", "word" )
#	def test_that_code_leveling_is_valid1(self):
#		self.assertRaises(ValueError, code_leveling.to_add_tuple, -8, -45 )


	def test_that_code_leveling2_exist(self):
		code_leveling.to_change_element_value	
		
	def test_that_code_leveling_exist2(self):
		code_leveling.convert_tuple_of_strings
		
	def test_that_code_leveling3_exist(self):
		code_leveling.unpacking_tuples	
	
	def test_that_code_leveling_exist3(self):
		code_leveling.suming_rows_of_2Dlist
		
	


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	