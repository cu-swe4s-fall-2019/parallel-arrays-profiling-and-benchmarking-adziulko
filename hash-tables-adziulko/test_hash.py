import unittest
import random
import hash_functions as hf


class Test_Hash_ascii(unittest.TestCase):
    def test_hash_ascii_one_word_small(self):
        r = hf.h_ascii('cyclistic', 50)
        self.assertEqual(r, 17)

    def test_hash_ascii_one_word_large(self):
        r = hf.h_ascii('cyclistic', 5000)
        self.assertEqual(r, 967)

    def test_hash_ascii_none_input(self):
        with self.assertRaises(TypeError):
            hf.h_ascii(None, random.randint(1, 10000))



class Test_Hash_rolling(unittest.TestCase):
    def test_hash_rolling_one_word_small(self):
        r = hf.h_rolling('cyclistic', 50)
        self.assertEqual(r, 39)

    def test_hash_rolling_one_word_large(self):
        r = hf.h_rolling('cyclistic', 5000)
        self.assertEqual(r, 3339)

    def test_hash_rolling_none_input(self):
        with self.assertRaises(TypeError):
            hf.h_rolling(None, 50)

    def test_hash_rolling_key_int(self):
        with self.assertRaises(TypeError):
            hf.h_rolling(50, 50)


class Test_Hash_Random_Function(unittest.TestCase):
    def test_hash_random_function_one_word_small(self):
        r = hf.random_h_function('cyclistic', 50)
        self.assertEqual(r, 17)

    def test_hash_random_function_one_word_large(self):
        r = hf.random_h_function('cyclistic', 5000)
        self.assertEqual(r, 2317)

    def test_hash_random_function_none_input(self):
        with self.assertRaises(TypeError):
            hf.random_h_function(None, 50)

    def test_hash_random_function_key_int(self):
        with self.assertRaises(TypeError):
            hf.h_rolling(50, 50)


if __name__ == '__main__':
    unittest.main()
