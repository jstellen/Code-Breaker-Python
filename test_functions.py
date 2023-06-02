import unittest

from mastermind import check_correctness, create_code, get_answer_input, take_turn
from unittest.mock import patch
from io import StringIO


class TestCode(unittest.TestCase):
    def test_create_code(self):
        for i in range(100):
            check_code = True
            code = create_code()
            self.assertEqual(len(code), 4)
            for i in range(4):
                if int(code[i]) in range(1,9):
                    check_code == True
                else:
                    check_code == False


    def test_check_correctness(self):
        correct = check_correctness(12, 4)
        correct = True
        self.assertTrue(correct)
    
    
    @patch("sys.stdin", StringIO("1234\n"))
    def test_get_answer_input(self):
        user_input = get_answer_input()
        self.assertEqual(user_input, "1234")

    
    @patch("sys.stdin", StringIO("1234\n"))
    def test_correct_digits_and_position(self):
        code = [1,2,3,4]
        answer = get_answer_input()
        position_and_digits = take_turn(code, answer)
        self.assertEqual(position_and_digits, (4,0))
    

    @patch("sys.stdin", StringIO("1234\n"))
    def test_correct_digits_only(self):
        code = [2,1,4,3]
        answer = get_answer_input()
        correct_only = take_turn(code, answer)
        self.assertEqual(correct_only, (0, 4))


if __name__ == '__main__':
    unittest.main()


    






