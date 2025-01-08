import unittest
from project import (
    generate_quick_password,
    generate_custom_password,
    check_password_strength
    )
import string

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_quick_password_positive(self):
        password = generate_quick_password(10)
        self.assertEqual(len(password), 10)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_quick_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_quick_password(0)

    def test_generate_custom_password_valid(self):
        password = generate_custom_password(5, 3, 2)
        self.assertEqual(len(password), 10)
        self.assertEqual(sum(char.isalpha() for char in password), 5)
        self.assertEqual(sum(char in string.punctuation for char in password), 3)
        self.assertEqual(sum(char.isdigit() for char in password), 2)

    def test_generate_custom_password_negative_input(self):
        with self.assertRaises(ValueError):
            generate_custom_password(-1, 3, 2)

    def test_generate_custom_password_zero_total_length(self):
        with self.assertRaises(ValueError):
            generate_custom_password(0, 0, 0)

    def test_check_password_strength_weak(self):
        self.assertEqual(check_password_strength("1234"), "Weak")

    def test_check_password_strength_medium(self):
        self.assertEqual(check_password_strength("A1!b2@c3#"), "Medium")

    def test_check_password_strength_strong(self):
        self.assertEqual(check_password_strength("StrongP@ssw0rd123!"), "Strong")

if __name__ == "__main__":
    unittest.main()
