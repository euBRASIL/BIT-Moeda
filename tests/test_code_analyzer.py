import unittest
import sys
import os

# Add the project root to sys.path to allow importing code_analyzer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from code_analyzer import execute_code

class TestCodeAnalyzer(unittest.TestCase):

    def test_valid_code(self):
        code = "print('Hello, world!')\na = 1 + 2\nprint(a)"
        success, error_message = execute_code(code)
        self.assertTrue(success)
        self.assertIsNone(error_message)

    def test_syntax_error(self):
        code = "print('Hello, world!'\na = 1 + " # Incomplete statement
        success, error_message = execute_code(code)
        self.assertFalse(success)
        self.assertIsNotNone(error_message)
        # Checking for a part of the generic SyntaxError message from ast.parse
        self.assertIn("invalid syntax", error_message.lower())

    def test_runtime_zero_division_error(self):
        code = "a = 1 / 0"
        success, error_message = execute_code(code)
        self.assertFalse(success)
        self.assertIsNotNone(error_message)
        self.assertIn("division by zero", error_message)

    def test_runtime_name_error(self):
        code = "print(undefined_variable)"
        success, error_message = execute_code(code)
        self.assertFalse(success)
        self.assertIsNotNone(error_message)
        self.assertIn("name 'undefined_variable' is not defined", error_message)

    def test_empty_code(self):
        code = ""
        success, error_message = execute_code(code)
        self.assertTrue(success) # Empty string is valid Python code
        self.assertIsNone(error_message)

    def test_code_with_imports(self):
        code = "import math\nprint(math.sqrt(4))"
        success, error_message = execute_code(code)
        self.assertTrue(success)
        self.assertIsNone(error_message)

if __name__ == '__main__':
    unittest.main()
