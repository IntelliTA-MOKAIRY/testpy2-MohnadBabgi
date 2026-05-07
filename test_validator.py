import unittest
from validator import is_valid_password

class TestValidator(unittest.TestCase):
    
    # Checkpoint 1 Test (Basic True/False)
    def test_basic_structure(self):
        self.assertFalse(is_valid_password(""), "An empty password should be False")

    # Checkpoint 2 Test (Length)
    def test_length(self):
        self.assertFalse(is_valid_password("short"), "Password must be at least 8 characters")
        self.assertTrue(is_valid_password("longenough"), "8+ characters should be valid so far")

    # Checkpoint 3 Test (Contains Number)
    def test_contains_number(self):
        self.assertFalse(is_valid_password("longenough"), "Password must contain a number")
        self.assertTrue(is_valid_password("longenough1"), "8+ characters with a number should be valid")

    # Checkpoint 4 Test (Contains '!')
    def test_special_char(self):
        self.assertFalse(is_valid_password("longenough1"), "Password must contain '!'")
        self.assertTrue(is_valid_password("longenough1!"), "Should be completely valid now")
