import unittest
import random
import hash_tables as ht
import hash_functions as hf


class Test_LP_Hash_Table(unittest.TestCase):
    def test_lp_hash_table_insert(self):
        lp_ht = ht.LPHashTable(random.randint(1, 10000), hf.h_ascii)
        lp_ht.add('cyclistic', 55)
        self.assertEqual(lp_ht.search('cyclistic'), 55)
        self.assertFalse(lp_ht.search('cyclist'), 55)


if __name__ == '__main__':
    unittest.main()
