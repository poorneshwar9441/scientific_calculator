import unittest
import logging
from unittest.mock import patch
from io import StringIO
from calculator import main

# Configure the logging module
logging.basicConfig(filename='logs/test_results.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestScientificCalculator(unittest.TestCase):

    def log_result(self, test_name, result):
        if result:
            logging.info(f"{test_name}: Passed")
        else:
            logging.error(f"{test_name}: Failed")

    @patch('builtins.input', side_effect=['1', '5', '3', '9'])
    def test_addition(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 8.0" in output
            self.log_result('test_addition', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['2', '5', '3', '9'])
    def test_subtraction(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 2.0" in output
            self.log_result('test_subtraction', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['3', '5', '3', '9'])
    def test_multiplication(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 15.0" in output
            self.log_result('test_multiplication', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['4', '6', '2', '9'])
    def test_division(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 3.0" in output
            self.log_result('test_division', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['5', '25', '9'])
    def test_square_root(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 5.0" in output
            self.log_result('test_square_root', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['6', '30', '9'])
    def test_sin(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 0.49999999999999994" in output
            self.log_result('test_sin', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['7', '60', '9'])
    def test_cos(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 0.5000000000000001" in output
            self.log_result('test_cos', result)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['8', '45', '9'])
    def test_tan(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            main()
            output = mock_output.getvalue()
            result = "Result: 0.9999999999999999" in output
            self.log_result('test_tan', result)
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()